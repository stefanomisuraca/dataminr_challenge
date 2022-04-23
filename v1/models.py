from ast import Call
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
    observer = models.JSONField(default=list)


class Alerts(TimeStampMixin):
    """Alerts model"""

    subscription = models.ForeignKey(Subscriptions, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(null=True)

    def send_alert(self) -> None:
        logger.info("Alert sent!")
        self.sent_date = datetime.now()
        self.save()

    def check_conditions(self, callback: Callable) -> None:
        return self.send_alert() if callback else logger.info("Condition not met yet")




