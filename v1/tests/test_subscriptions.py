from django.test import TestCase
from rest_framework.test import RequestsClient

class AnimalTestCase(TestCase):
    fixtures = ["subscriptions.json"]

    def test_animals_can_speak(self):
        request = self.client.get('http://testserver/v1/subscriptions/')
        result = request.json()
        self.assertEqual(request.status_code, 200)

