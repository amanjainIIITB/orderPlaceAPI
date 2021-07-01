from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .helper import DeliveryCharge


# Create your views here.
class Order(APIView):
    def __init__(self):
        self.order_items_charges = 0
        self.delivery_charge = 0
        self.discount = 0
        self.total_charge = 0

    def compute_order_items_charges(self, order_items):
        for order_item in order_items:
            self.order_items_charges = self.order_items_charges + order_item['price'] * order_item['quantity']

    def post(self, request):
        try:
            if 'order_items' not in request.data:
                return Response({'Error': 'Order Items not found, please add order items'})
            elif 'distance' not in request.data:
                return Response({'Error': 'Please enter Delivery Address'})
            elif request.data['distance'] > 500000:
                return Response({'Error': 'We do not deliver at the given location'})
            else:
                self.compute_order_items_charges(request.data['order_items'])
                obj = DeliveryCharge(0, 0, 0)
                if 'offer' in request.data and 'offer_type' in request.data['offer']:
                    offer = request.data['offer']
                    if offer['offer_type'] == 'FLAT' and 'offer_val' in offer:
                        if offer['offer_val'] < 0:
                            return Response({'Error': 'offer value cannot be less than 0'})
                        else:
                            self.delivery_charge = obj.getDeliveryCharge(request.data['distance'])
                            self.discount = min(offer['offer_val'], self.order_items_charges)
                    elif offer['offer_type'] == 'DELIVERY':
                        self.discount = self.delivery_charge
                else:
                    self.delivery_charge = obj.getDeliveryCharge(request.data['distance'])
                self.total_charge = self.order_items_charges + self.delivery_charge - self.discount
                return Response({'order_total': self.total_charge})
        except:
            return Response({'Error': 'Contact System Administrator'})
