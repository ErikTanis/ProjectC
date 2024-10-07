from repositories.base_repository import BaseRepository
from models.item_groups import ItemGroup

JSON_FILE_NAME = "item_lines.json"


class ItemGroupsRepository(BaseRepository):
    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def get_all(self):
        return list(self.entries.values())

    def get_by_id(self, item_group_id):
        return self.entries.get(item_group_id)

    def add(self, item_group):
        if item_group.id in self.entries:
            return False

        item_group.created_at = self.get_timestamp()
        item_group.updated_at = self.get_timestamp()
        self.entries[item_group.id] = item_group
        self.save()
        return True

    def update(self, item_group_id, item_group):
        if item_group_id not in self.entries:
            return False

        item_group.updated_at = self.get_timestamp()
        self.entries[item_group_id] = item_group
        self.save()
        return True

    def remove(self, item_group_id):
        if item_group_id not in self.entries:
            return False

        self.entries.pop(item_group_id, None)
        self.save()
        return True

    def load(self):
        self.entries = {entry['id']: ItemGroup.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])