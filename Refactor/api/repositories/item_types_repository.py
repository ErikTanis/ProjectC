from repositories.base_repository import BaseRepository
from models.item_types import ItemType

JSON_FILE_NAME = "item_types.json"


class ItemTypesRepository(BaseRepository):

    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def get_all(self):
        return list(self.entries.values())

    def get_by_id(self, item_type_id):
        return self.entries.get(item_type_id)

    def add(self, item_type):
        if item_type.id in self.entries:
            return False

        item_type.created_at = self.get_timestamp()
        item_type.updated_at = self.get_timestamp()
        self.entries[item_type.id] = item_type
        self.save()
        return True

    def update(self, item_type_id, item_type):
        if item_type_id not in self.entries:
            return False

        item_type.updated_at = self.get_timestamp()
        self.entries[item_type_id] = item_type
        self.save()
        return True

    def remove(self, item_type_id):
        if item_type_id not in self.entries:
            return False

        self.entries.pop(item_type_id, None)
        self.save()
        return True

    def load(self):
        self.entries = {entry['id']: ItemType.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])
