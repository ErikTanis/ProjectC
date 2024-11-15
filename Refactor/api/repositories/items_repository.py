from repositories.base_repository import BaseRepository
from models.items import Item

JSON_FILE_NAME = "items.json"


class ItemsRepository(BaseRepository):
    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def get_all(self):
        return list(self.entries.values())

    def get_all_by_item_line(self, item_line_id):
        return [entry for entry in self.entries.values() if entry.item_line == item_line_id]

    def get_all_by_item_group(self, item_group_id):
        return [entry for entry in self.entries.values() if entry.item_group == item_group_id]

    def get_all_by_item_type(self, item_type_id):
        return [entry for entry in self.entries.values() if entry.item_type == item_type_id]

    def get_all_by_supplier(self, supplier_id):
        return [entry for entry in self.entries.values() if entry.supplier_id == supplier_id]

    def get_by_id(self, item_id):
        return self.entries.get(item_id)

    def add(self, item):
        if item.uid in self.entries:
            return False

        item.created_at = self.get_timestamp()
        item.updated_at = self.get_timestamp()
        self.entries[item.uid] = item
        self.save()
        return True

    def update(self, item_id, item):
        if item.uid not in self.entries:
            return False

        item.updated_at = self.get_timestamp()
        self.entries[item_id] = item
        self.save()
        return True

    def remove(self, item_id):
        if item_id not in self.entries:
            return False

        self.entries.pop(item_id, None)
        self.save()
        return True

    def load(self):
        self.entries = {entry['uid']: Item.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])
