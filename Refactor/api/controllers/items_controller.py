from api.providers import repository_provider
from base_controller import BaseController
from api.models.items import Item


class ItemsController(BaseController):
    def __init__(self):
        self.provider = repository_provider

    def handle_get_version_1(self, path, handler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                self.get_by_id(path[1], handler)
            case 3:
                self.get_inventory_by_item_id(path[1], handler)
            case 4:
                self.get_inventory_totals_by_item_id(path[1], handler)
            case _:
                self.respond_not_found(handler)

    def handle_post_version_1(self, handler):
        self.add(handler)

    def handle_put_version_1(self, path, handler):
        self.update(path, handler)

    def handle_delete_version_1(self, path, handler):
        self.delete(path, handler)

    # /api/v1/items
    def get_all(self, handler):
        items = self.provider.fetch_item_pool().get_all()
        self.respond_ok(handler, items)

    # /api/v1/items/{item_id}
    def get_by_id(self, item_id, handler):
        items = self.provider.fetch_item_pool().get_by_id(item_id)
        self.respond_ok(handler, items)

    # /api/v1/items/{item_id}/inventory
    def get_inventory_by_item_id(self, item_id, handler):
        inventories = self.provider.fetch_inventory_pool().get_all_by_item_id(item_id)
        self.respond_ok(handler, inventories)

    # /api/v1/items/{item_id}/inventory/totals
    def get_inventory_totals_by_item_id(self, item_id, handler):
        totals = self.provider.fetch_inventory_pool().get_totals_by_item_id(item_id)
        self.respond_ok(handler, totals)

    # /api/v1/items
    def add(self, handler):
        content = self.get_json_body(handler)
        item = Item.from_dict(content)
        self.provider.fetch_item_pool().add_item(item)
        self.respond_created(handler, item)

    # /api/v1/items/{item_id}
    def update(self, path, handler):
        item_id = int(path[1])
        content = self.get_json_body(handler)
        item = Item.from_dict(content)
        self.provider.fetch_item_pool().update(item_id, item)
        self.respond_ok(handler)

    # /api/v1/items/{item_id}
    def delete(self, path, handler):
        item_id = int(path[1])
        self.provider.fetch_item_pool().remove(item_id)
        self.respond_ok(handler)