import json

# Opening JSON file
class DeliveryCharge:
    def __init__(self, start_distance, end_distance, charge):
        self.start_distance = start_distance
        self.end_distance = end_distance
        self.charge = charge

    def computeDeliveryCharge(self, start_index, end_index, distance, deliverCharges):
        mid = start_index + (end_index - start_index) // 2
        if deliverCharges[mid].start_distance <= distance < deliverCharges[mid].end_distance:
            return deliverCharges[mid].charge
        elif distance >= deliverCharges[mid].end_distance:
            return self.computeDeliveryCharge(mid, end_index, distance, deliverCharges)
        else:
            return self.computeDeliveryCharge(start_index, mid, distance, deliverCharges)

    def getDeliveryCharge(self, distance):
        return self.computeDeliveryCharge(0, len(delivery_charges), distance, delivery_charges)


with open('delivery_charge_config.json') as json_file:
    delivery_charge_configs = json.load(json_file)
    delivery_charges = list()
    for delivery_charge_config in delivery_charge_configs:
        delivery_charge = delivery_charge_configs[delivery_charge_config]
        delivery_charges.append(DeliveryCharge(delivery_charge['start_distance'], delivery_charge['end_distance'], delivery_charge['charge']))
