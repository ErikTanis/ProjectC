from api.providers import repository_provider
from base_controller import BaseController
from api.models.item_groups import ItemGroup


class ItemGroupsController(BaseController):
    def __init__(self):
        self.provider = repository_provider

    def handle_get_version_1(self, path, handler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                item_group_id = int(path[1])
                self.get_by_id(handler, item_group_id)
            case 3:
                if path[2] == "items":
                    item_group_id = int(path[1])
                    self.get_items_by_item_group_id(handler, item_group_id)
                else:
                    self.respond_not_found(handler)
            case _:
                self.respond_not_found(handler)

    def handle_post_version_1(self, path, handler):
        # not implemented in original main.py
        pass

    def handle_put_version_1(self, path, handler):
        item_group_id = int(path[1])
        self.update(handler, item_group_id)

    def handle_delete_version_1(self, path, handler):
        item_group_id = int(path[1])
        self.delete(handler, item_group_id)

    # /api/v1/item_groups
    def get_all(self, handler):
        item_groups = self.provider.fetch_item_group_pool().get_all()
        self.respond_ok(handler, item_groups)

    # /api/v1/item_groups/{item_group_id}
    def get_by_id(self, handler, item_group_id):
        item_group = self.provider.fetch_item_group_pool().get_by_id(item_group_id)
        self.respond_ok(handler, item_group)

    # /api/v1/item_groups/{item_group_id}/items
    def get_items_by_item_group_id(self, handler, item_group_id):
        items = self.provider.fetch_item_pool().get_all_by_item_group(item_group_id)
        self.respond_ok(handler, items)

    # /api/v1/item_groups/{item_group_id}
    def update(self, handler, item_group_id):
        data = self.get_json_body(handler)
        updated_item_group = ItemGroup.from_dict(data)
        self.provider.fetch_item_group_pool().update(item_group_id, updated_item_group)
        self.respond_ok(handler)

    # /api/v1/item_groups/{item_group_id}
    def delete(self, handler, item_group_id):
        self.provider.fetch_item_group_pool().remove(item_group_id)
        self.respond_ok(handler)
