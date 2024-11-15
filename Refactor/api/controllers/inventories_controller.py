from api.providers import repository_provider
from base_controller import BaseController
from api.models.inventories import Inventory


class InventoriesController(BaseController):
    def __init__(self):
        self.provider = repository_provider

    def handle_get_version_1(self, path, handler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                inventory_id = int(path[1])
                self.get_by_id(handler, inventory_id)
            case _:
                self.respond_not_found(handler)

    def handle_post_version_1(self, handler):
        self.add(handler)

    def handle_put_version_1(self, path, handler):
        inventory_id = int(path[1])
        self.update(handler, inventory_id)

    def handle_delete_version_1(self, path, handler):
        inventory_id = int(path[1])
        self.delete(handler, inventory_id)

    # /api/v1/inventories
    def get_all(self, handler):
        inventories = self.provider.fetch_inventory_pool().get_all()
        self.respond_ok(handler, inventories)

    # /api/v1/inventories/{inventory_id}
    def get_by_id(self, handler, inventory_id):
        inventories = self.provider.fetch_inventory_pool().get_by_id(inventory_id)
        self.respond_ok(handler, inventories)

    # /api/v1/inventories
    def add(self, handler):
        content = self.get_json_body(handler)
        inventory = Inventory.from_dict(content)
        self.provider.fetch_inventory_pool().add(inventory)
        self.respond_ok(handler, inventory)

    # /api/v1/inventories/{inventory_id}
    def update(self, handler, inventory_id):
        content = self.get_json_body(handler)
        inventory = Inventory.from_dict(content)
        self.provider.fetch_inventory_pool().update(inventory_id, inventory)
        self.respond_ok(handler, inventory)

    # /api/v1/inventories/{inventory_id}
    def delete(self, handler, inventory_id):
        self.provider.fetch_inventory_pool().remove(inventory_id)
        self.respond_ok(handler, None)