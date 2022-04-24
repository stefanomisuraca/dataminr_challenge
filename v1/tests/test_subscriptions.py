import json
from django.test import TestCase
from rest_framework.test import APIClient
from v1.models import Subscriptions

class SubscriptionsTestCase(TestCase):
    fixtures = ["subscriptions.json"]
    def setUp(self) -> None:
        self.apiClient = APIClient()

    def test_get_list_subscriptions(self):
        request = self.apiClient.get('http://testserver/v1/subscriptions/')
        result = request.json()
        self.assertEqual(request.status_code, 200)
        self.assertIsInstance(result.get("results"), list)
    
    def test_get_retrive_subscription(self):
        request = self.apiClient.get('http://testserver/v1/subscriptions/1/')
        result = request.json()
        self.assertEqual(request.status_code, 200)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get("id"), 1)

    def test_post_subscription(self):
        payload = {
            "address": "myaddress@gmail.com",
            "location": "Paris",
            "observers": json.dumps([{"key": "temp", "target": 10, "condition": "equal"}])
        }
        request = self.apiClient.post('http://testserver/v1/subscriptions/', format="json", data=payload)
        result = request.data
        self.assertEqual(request.status_code, 201)
        self.assertEqual(result.get("id"), 3)

    def test_post_subscription_failed(self):
        payload = {
            "address": "wrongEmail",
            "location": "Paris",
            "observers": [{"key": "temp", "target": 10, "condition": "equal"}]
        }
        error = {'address': ['Enter a valid email address.']}
        request = self.apiClient.post('http://testserver/v1/subscriptions/', format="json", data=payload)
        self.assertEqual(request.status_code, 400)
        self.assertDictEqual(request.json(), error)

    def test_delete_subscription(self):
        request = self.apiClient.delete('http://testserver/v1/subscriptions/2/')
        self.assertEqual(request.status_code, 204)
        subscription = Subscriptions.objects.filter(id=2).exists()
        self.assertFalse(subscription)

    def test_get_subscription_not_found(self):
        request = self.apiClient.get('http://testserver/v1/subscriptions/45/')
        self.assertEqual(request.status_code, 404)
    
    def test_edit_subscription_edit(self):

        new_payload = {
            "address": "anotherEmail@gmail.com",
            "location": "Rome",
            "observers": [{"key": "temp", "target": 9, "condition": "below"}]
        }
        
        request_old = self.apiClient.get('http://testserver/v1/subscriptions/2/')
        result_old = request_old.json()       
        self.assertEqual(request_old.status_code, 200)
        self.assertEqual(result_old.get("id"), 2)

        
        request_new = self.apiClient.put('http://testserver/v1/subscriptions/2/', format="json", data=new_payload)
        result_new = request_new.data
        self.assertEqual(request_new.status_code, 200)
        self.assertEqual(result_old.get("id"), result_new.get("id"))
