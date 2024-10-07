from Refactor.api.providers import repository_provider
from repositories.base_repository import BaseRepository
from models.shipments import Shipment

JSON_FILE_NAME = "shipments.json"


class ShipmentsRepository(BaseRepository):
    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def load(self):
        self.entries = {entry['id']: Shipment.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])

    def get_shipments(self) -> list[Shipment]:
        return list(self.entries.values())
    
    def get_shipment(self, shipment_id):
        if shipment_id in self.entries:
            return self.entries[shipment_id]
        return None

    def get_items_in_shipment(self, shipment_id):
        if shipment_id in self.entries:
            return self.entries[shipment_id].items
        return None

    def add_shipment(self, shipment: Shipment):
        shipment["created_at"] = self.get_timestamp()
        shipment["updated_at"] = self.get_timestamp()
        self.entries[shipment.id] = shipment

    def update_shipment(self, shipment_id, shipment):
        shipment["updated_at"] = self.get_timestamp()
        if shipment_id in self.entries:
            self.entries[shipment_id] = shipment

    def update_items_in_shipment(self, shipment_id, items):
        shipment = self.get_shipment(shipment_id)
        current = shipment["items"]
        for x in current:
            found = False
            for y in items:
                if x["item_id"] == y["item_id"]:
                    found = True
                    break
            if not found:
                inventories = repository_provider.fetch_inventory_pool(
                ).get_inventories_for_item(x["item_id"])
                max_ordered = -1
                max_inventory
                for z in inventories:
                    if z["total_ordered"] > max_ordered:
                        max_ordered = z["total_ordered"]
                        max_inventory = z
                max_inventory["total_ordered"] -= x["amount"]
                max_inventory["total_expected"] = y["total_on_hand"] + \
                    y["total_ordered"]
                repository_provider.fetch_inventory_pool().update_inventory(
                    max_inventory["id"], max_inventory)
        for x in current:
            for y in items:
                if x["item_id"] == y["item_id"]:
                    inventories = repository_provider.fetch_inventory_pool(
                    ).get_inventories_for_item(x["item_id"])
                    max_ordered = -1
                    max_inventory
                    for z in inventories:
                        if z["total_ordered"] > max_ordered:
                            max_ordered = z["total_ordered"]
                            max_inventory = z
                    max_inventory["total_ordered"] += y["amount"] - x["amount"]
                    max_inventory["total_expected"] = y["total_on_hand"] + \
                        y["total_ordered"]
                    repository_provider.fetch_inventory_pool().update_inventory(
                        max_inventory["id"], max_inventory)
        shipment["items"] = items
        self.update_shipment(shipment_id, shipment)

    def remove_shipment(self, shipment_id):
        if shipment_id in self.entries:
            del self.entries[shipment_id]
