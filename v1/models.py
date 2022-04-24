from datetime import datetime
from django.db import models
from typing import Callable

import logging
logger = logging.getLogger("dataminr")

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Subscriptions(TimeStampMixin):
    """Subscription model"""
   
    address = models.EmailField(max_length=254)
    location = models.CharField(max_length=254)
    observers = models.JSONField(default=list)


class Alerts(TimeStampMixin):
    """Alerts model"""

    subscription = models.ForeignKey(Subscriptions, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(null=True)

    def send_alert(self) -> bool:
        logger.info("Alert sent!")
        self.sent_date = datetime.now()
        self.save()
        return True
    
    def condition_not_met(self) -> bool:
        logger.info("Condition not met yet")
        return False

    def check_conditions(self, callback: Callable) -> bool:
        return self.send_alert() if callback else self.condition_not_met()




