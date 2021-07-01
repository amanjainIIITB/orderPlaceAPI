from django.test import TestCase, Client
import json

class InvalidOrder(TestCase):
    client = Client()

    def test_distance_not_found(self):
        order = {
            "order_items": [
                {
                    "name": "bread",
                    "quantity": 2,
                    "price": 2200
                },
                {
                    "name": "butter",
                    "quantity": 1,
                    "price": 5900
                }
            ],
            "offer": {
                "offer_type": "FLAT",
                "offer_val": 1000
            }
        }
        response = self.client.post('/order/', json.dumps(order), content_type="application/json")
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'Error': 'Please enter Delivery Address'})

    def test_exceed_distance(self):
        order = {
            "order_items": [
                {
                    "name": "bread",
                    "quantity": 2,
                    "price": 2200
                },
                {
                    "name": "butter",
                    "quantity": 1,
                    "price": 5900
                }
            ],
            "distance": 500001,
            "offer": {
                "offer_type": "FLAT",
                "offer_val": 1000
            }
        }
        response = self.client.post('/order/', json.dumps(order), content_type="application/json")
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'Error': 'We do not deliver at the given location'})

    def test_NEGATIVE_offer_value(self):
        order = {
            "order_items": [
                {
                    "name": "bread",
                    "quantity": 2,
                    "price": 2200
                },
                {
                    "name": "butter",
                    "quantity": 1,
                    "price": 5900
                }
            ],
            "distance": 1200,
            "offer": {
                "offer_type": "FLAT",
                "offer_val": -1000
            }
        }
        response = self.client.post('/order/', json.dumps(order), content_type="application/json")
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'Error': 'offer value cannot be less than 0'})

    def test_order_items_not_found(self):
        order = {
            "distance": 500000,
            "offer": {
                "offer_type": "FLAT",
                "offer_val": 1000
            }
        }
        response = self.client.post('/order/', json.dumps(order), content_type="application/json")
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'Error': 'Order Items not found, please add order items'})
