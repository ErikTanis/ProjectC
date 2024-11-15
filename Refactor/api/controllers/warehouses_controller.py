from api.providers import repository_provider
from Base_controller import BaseController
from api.models.warehouses import Warehouse

class WarehousesController(BaseController):
    def __init__(self):
        self.provider = repository_provider

    def handle_get_version_1(self, path, handler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                warehouse_id = int(path[1])
                self.get_by_id(handler, warehouse_id)
            case _:
                self.respond_not_found(handler)

    def handle_post_version_1(self, handler):
        self.add(handler)

    def handle_put_version_1(self, path, handler):
        warehouse_id = int(path[1])
        self.update(handler, warehouse_id)

    def handle_delete_version_1(self, path, handler):
        warehouse_id = int(path[1])
        self.delete(handler, warehouse_id)

    # /api/v1/warehouses
    def get_all(self, handler):
        warehouses = self.provider.fetch_warehouse_pool().get_all()
        self.respond_ok(handler, warehouses)

    # /api/v1/warehouses/{warehouse_id}
    def get_by_id(self, handler, warehouse_id):
        warehouse = self.provider.fetch_warehouse_pool().get_by_id(warehouse_id)
        self.respond_ok(handler, warehouse)

    # /api/v1/warehouses
    def add(self, handler):
        content = self.get_json_body(handler)
        warehouse = Warehouse.from_dict(content)
        self.provider.fetch_warehouse_pool().add(warehouse)
        self.respond_ok(handler, warehouse)

    # /api/v1/warehouses/{warehouse_id}
    def update(self, handler, warehouse_id):
        content = self.get_json_body(handler)
        warehouse = Warehouse.from_dict(content)
        self.provider.fetch_warehouse_pool().update(warehouse_id, warehouse)
        self.respond_ok(handler, warehouse)

    # /api/v1/warehouses/{warehouse_id}
    def delete(self, handler, warehouse_id):
        self.provider.fetch_warehouse_pool().remove(warehouse_id)
        self.respond_ok(handler, None)