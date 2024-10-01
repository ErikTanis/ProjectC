import json

class WarehousesRepository(BaseRepository):
    def __init__(self):
        super().__init__("warehouses.json", False)
        self.load()

    def get_warehouses(self):
        return self.warehouses

    def get(self, warehouse_id):
        for x in self.warehouses:
            if x["id"] == warehouse_id:
                return x
        return None

    def add(self, warehouse):
        warehouse["created_at"] = self.get_timestamp()
        warehouse["updated_at"] = self.get_timestamp()
        self.warehouses.append(warehouse)
        self.save()

    def update(self, warehouse_id, warehouse):
        warehouse["updated_at"] = self.get_timestamp()
        for i in range(len(self.warehouses)):
            if self.warehouses[i]["id"] == warehouse_id:
                self.warehouses[i] = warehouse
                break
        self.save()

    def remove(self, warehouse_id):
        for x in self.warehouses:
            if x["id"] == warehouse_id:
                self.warehouses.remove(x)
        self.save()

    def load(self):
        data = super().load()
        self.warehouses = []
        for x in data:
            self.warehouses.append(Warehouse(**x))

    def save(self):
        data = []
        for x in self.warehouses:
            data.append(x.__dict__)
        super().save(data)