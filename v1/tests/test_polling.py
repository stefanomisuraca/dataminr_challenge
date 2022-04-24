import json
from re import sub
from django.test import TestCase
from rest_framework.test import APIClient
from v1.models import Alerts, Subscriptions
from v1.polling import polling_weather

class PollingTestCase(TestCase):
    fixtures = ["subscriptions.json"]

    def setUp(self) -> None:
        self.subscription = Subscriptions(
            address="test@email.com",
            location="nonExistingLocation",
            observers=[{"key": "temp", "target": 1, "condition": "below"}]
        )
        self.subscription.save()

    def test_polling_location_not_found(self):
        result = polling_weather(subscription=self.subscription)
        for i in result:
            self.assertIsNone(i)
    
    def test_polling_condition_not_met(self):
        self.subscription.location = "Rome,it"
        self.subscription.save()

        result = polling_weather(subscription=self.subscription)
        for count, condition in result:
           self.assertIsInstance(count, int)
           self.assertFalse(condition)
           if count == 5:
               break

    def test_polling_success(self):
        self.subscription.location = "Rome,it"
        self.subscription.observers = [{"key": "temp", "target": 5, "condition": "above"}]
        self.subscription.save()

        result = polling_weather(subscription=self.subscription)
        for count, condition in result:
           self.assertIsInstance(count, int)
           self.assertTrue(condition)
           if count == 5:
               alerts = Alerts.objects.filter(subscription=self.subscription).count()
               self.assertEqual(alerts, 5)
               break