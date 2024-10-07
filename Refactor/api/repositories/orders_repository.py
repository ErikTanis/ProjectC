from Refactor.api.providers import repository_provider
from repositories.base_repository import BaseRepository
from models.orders import Order
from models.items import Item

JSON_FILE_NAME = "orders.json"

class OrdersRepository(BaseRepository):
    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def load(self):
        self.entries = {entry['id']: Order.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])

    def get_orders(self) -> list[Order]:
        return list(self.entries.values())

    def get_order(self, id) -> Order:
        if id in self.entries:
            return self.entries[id]
        return None
    
    def get_items_in_order(self, order_id) -> list[Order]:
        if order_id in self.entries:
            return self.entries[order_id].items

    def get_orders_in_shipment(self, shipment_id):
        [order for order in self.entries.values() if order.shipment_id == shipment_id]

    def get_orders_for_client(self, client_id):
        [order for order in self.entries.values() if order.source_id == client_id]

    def add_order(self, order: Order):
        if not isinstance(order, Order):
            raise TypeError("order must be an instance of Order")
        order.created_at = self.get_timestamp()
        order.updated_at = self.get_timestamp()
        self.entries[order.id] = order
        self.save()

    def update_order(self, order_id: int, order: Order):
        if not isinstance(order, Order):
            raise TypeError("order must be an instance of Order")
        order["updated_at"] = self.get_timestamp()
        if order_id in self.entries:
            self.entries[order_id] = order
    
    def update_items_in_order(self, order_id, items: list[Item]):
        if not isinstance(items, list):
            raise TypeError("items must be a list")
        for item in items:
            if not isinstance(item, Item):
                raise TypeError("item must be an instance of Item")
        order = self.get_order(order_id)
        current = order["items"]
        for x in current:
            found = False
            for y in items:
                if x["item_id"] == y["item_id"]:
                    found = True
                    break
            if not found:
                inventories = repository_provider.fetch_inventory_pool(
                ).get_inventories_for_item(x["item_id"])
                min_ordered = 1_000_000_000_000_000_000
                min_inventory
                for z in inventories:
                    if z["total_allocated"] > min_ordered:
                        min_ordered = z["total_allocated"]
                        min_inventory = z
                min_inventory["total_allocated"] -= x["amount"]
                min_inventory["total_expected"] = y["total_on_hand"] + \
                    y["total_ordered"]
                repository_provider.fetch_inventory_pool().update_inventory(
                    min_inventory["id"], min_inventory)
        for x in current:
            for y in items:
                if x["item_id"] == y["item_id"]:
                    inventories = repository_provider.fetch_inventory_pool(
                    ).get_inventories_for_item(x["item_id"])
                    min_ordered = 1_000_000_000_000_000_000
                    min_inventory
                    for z in inventories:
                        if z["total_allocated"] < min_ordered:
                            min_ordered = z["total_allocated"]
                            min_inventory = z
                min_inventory["total_allocated"] += y["amount"] - x["amount"]
                min_inventory["total_expected"] = y["total_on_hand"] + \
                    y["total_ordered"]
                repository_provider.fetch_inventory_pool().update_inventory(
                    min_inventory["id"], min_inventory)
        order["items"] = items
        self.update_order(order_id, order)
        

    def update_orders_in_shipment(self, shipment_id, orders):
        packed_orders = self.get_orders_in_shipment(shipment_id)
        for x in packed_orders:
            if x not in orders:
                order = self.get_order(x)
                order["shipment_id"] = -1
                order["order_status"] = "Scheduled"
                self.update_order(x, order)
        for x in orders:
            order = self.get_order(x)
            order["shipment_id"] = shipment_id
            order["order_status"] = "Packed"
            self.update_order(x, order)

    def remove_order(self, id):
        if id in self.entries:
            del self.entries[id]
