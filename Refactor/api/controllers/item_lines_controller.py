from api.providers import repository_provider
from base_controller import BaseController
from api.models.item_lines import ItemLine


class ItemLinesController(BaseController):
    def __init__(self) -> None:
        self.provider = repository_provider

    def handle_get_version_1(self, path, handler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                itemLineId = int(path[1])
                self.get_by_id(handler, itemLineId)
            case 3:
                if (path[2] == "items"):
                    itemLineId = int(path[1])
                    self.get_items_by_item_line_id(handler, itemLineId)
                else:
                    self.respond_not_found(handler)
            case _:
                self.respond_not_found(handler)

    def handle_post_version_1(self, handler):
        # not implemented in original main.py
        pass

    def handle_put_version_1(self, path, handler):
        itemLineId = int(path[1])
        self.update(path, handler, itemLineId)

    def handle_delete_version_1(self, path, handler):
        itemLineId = int(path[1])
        self.delete(path, handler, itemLineId)

    # /api/v1/item_lines
    def get_all(self, handler):
        itemLines = self.provider.fetch_item_line_pool().get_all()
        self.respond_ok(handler, itemLines)

    # /api/v1/item_lines/{item_line_id}
    def get_by_id(self, handler, item_id):
        itemLine = self.provider.fetch_item_line_pool().get_by_id(item_id)
        self.respond_ok(handler, itemLine)

    # /api/v1/item_lines/{item_line_id}/items
    def get_items_by_item_line_id(self, handler, item_line_id):
        items = self.provider.fetch_item_pool().get_all_by_item_line(item_line_id)
        self.respond_ok(handler, items)

    # /api/v1/item_lines/{item_line_id}
    def update(self, handler, item_line_id):
        data = self.get_json_body(handler)
        updated_item_line = ItemLine.from_dict(data)
        self.provider.fetch_item_line_pool().update(item_line_id, updated_item_line)
        self.respond_ok(handler)

    # /api/v1/item_lines/{item_line_id}
    def delete(self, handler, item_line_id):
        self.provider.fetch_item_line_pool().remove(item_line_id)
        self.respond_no_content(handler)
