from repositories.base_repository import BaseRepository
from models.inventories import Inventory
from collections import defaultdict

JSON_FILE_NAME = "inventories.json"


class InventoriesRepository(BaseRepository):
    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def get_all(self):
        return list(self.entries.values())

    def get_by_id(self, inventory_id):
        return self.entries.get(inventory_id)

    def get_all_by_item_id(self, item_id):
        return [entry for entry in self.entries.values() if entry.item_id == item_id]

    def get_totals_by_item_id(self, item_id):
        totals = defaultdict(int)

        for entry in self.get_all_by_item_id(item_id):
            totals["total_expected"] += entry.total_expected
            totals["total_ordered"] += entry.total_ordered
            totals["total_allocated"] += entry.total_allocated
            totals["total_available"] += entry.total_available

        return dict(totals)

    def add(self, inventory):
        if inventory.id in self.entries:
            return False

        inventory.created_at = self.get_timestamp()
        inventory.updated_at = self.get_timestamp()
        self.entries[inventory.id] = inventory
        self.save()
        return True

    def update(self, inventory_id, inventory):
        if inventory_id not in self.entries:
            return False

        inventory.updated_at = self.get_timestamp()
        self.entries[inventory_id] = inventory
        self.save()
        return True

    def remove(self, inventory_id):
        if inventory_id not in self.entries:
            return False

        self.entries.pop(inventory_id, None)
        self.save()
        return True

    def load(self):
        self.entries = {entry['id']: Inventory.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])
