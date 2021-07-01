from django.test import TestCase, Client
import json

class ValidOrder(TestCase):
    client = Client()

    def test_FLAT_offer(self):
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
                "offer_val": 1000
            }
        }
        response = self.client.post('/order/', json.dumps(order), content_type="application/json")
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'order_total': 14300})

    def test_DELIVERY_offer(self):
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
                "offer_type": "DELIVERY"
            }
        }
        response = self.client.post('/order/', json.dumps(order), content_type="application/json")
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'order_total': 10300})

    def test_NO_offer(self):
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
        }
        response = self.client.post('/order/', json.dumps(order), content_type="application/json")
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data, {'order_total': 15300})
