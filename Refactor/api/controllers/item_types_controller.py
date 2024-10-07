from api.providers import repository_provider
from base_controller import BaseController
from api.models.item_types import ItemType


class ItemTypesController(BaseController):
    def __init__(self):
        self.provider = repository_provider

    def handle_get_version_1(self, path, handler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                item_type_id = int(path[1])
                self.get_by_id(handler, item_type_id)
            case 3:
                if path[2] == "items":
                    item_type_id = int(path[1])
                    self.get_items_by_item_type_id(handler, item_type_id)
                else:
                    self.respond_not_found(handler)
            case _:
                self.respond_not_found(handler)

    def handle_post_version_1(self, handler):
        # not implemented in original main.py
        pass

    def handle_put_version_1(self, path, handler):
        item_type_id = int(path[1])
        self.update(handler, item_type_id)

    def handle_delete_version_1(self, path, handler):
        item_type_id = int(path[1])
        self.delete(handler, item_type_id)

    # /api/v1/item_types
    def get_all(self, handler):
        item_types = self.provider.fetch_item_type_pool().get_all()
        self.respond_ok(handler, item_types)

    # /api/v1/item_types/{item_type_id}
    def get_by_id(self, handler, item_type_id):
        item_type = self.provider.fetch_item_type_pool().get_by_id(item_type_id)
        self.respond_ok(handler, item_type)

    # /api/v1/item_types/{item_type_id}/items
    def get_items_by_item_type_id(self, handler, item_type_id):
        items = self.provider.fetch_item_pool().get_all_by_item_type(item_type_id)
        self.respond_ok(handler, items)

    # /api/v1/item_types/{item_type_id}
    def update(self, handler, item_type_id):
        content = self.get_request_content(handler)
        item_type = ItemType.from_dict(content)
        self.provider.fetch_item_type_pool().update(item_type_id, item_type)
        self.respond_ok(handler, item_type)

    # /api/v1/item_types/{item_type_id}
    def delete(self, handler, item_type_id):
        self.provider.fetch_item_type_pool().remove(item_type_id)
        self.respond_ok(handler)
