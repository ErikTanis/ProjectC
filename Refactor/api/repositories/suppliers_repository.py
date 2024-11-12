from repositories.base_repository import BaseRepository
from models.suppliers import Supplier

JSON_FILE_NAME = "suppliers.json"

class SuppliersRepository(BaseRepository):
    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def load(self):
        self.entries = {entry['id']: Supplier.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])

    def get_suppliers(self):
        return self.entries

    def get_supplier(self, supplier_id):
        if supplier_id in self.entries:
            return self.entries[supplier_id]
        return None

    def add_supplier(self, supplier: Supplier):
        supplier["created_at"] = self.get_timestamp()
        supplier["updated_at"] = self.get_timestamp()
        self.entries[supplier.id] = supplier

    def update_supplier(self, supplier_id: int, supplier: Supplier):
        supplier["updated_at"] = self.get_timestamp()
        if supplier_id in self.entries:
            self.entries[supplier_id] = supplier

    def remove_supplier(self, supplier_id):
        if supplier_id in self.entries:
            del self.entries[supplier_id]
