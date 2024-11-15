from repositories.base_repository import BaseRepository
from models.item_lines import ItemLine

JSON_FILE_NAME = "item_lines.json"


class ItemLinesRepository(BaseRepository):

    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def get_all(self):
        return list(self.entries.values())

    def get_by_id(self, item_line_id):
        return self.entries.get(item_line_id)

    def add(self, item_line):
        if item_line.id in self.entries:
            return False

        item_line.created_at = self.get_timestamp()
        item_line.updated_at = self.get_timestamp()
        self.entries[item_line.id] = item_line
        self.save()
        return True

    def update(self, item_line_id, item_line):
        if item_line_id not in self.entries:
            return False

        item_line.updated_at = self.get_timestamp()
        self.entries[item_line_id] = item_line
        self.save()
        return True

    def remove(self, item_line_id):
        if item_line_id not in self.entries:
            return False

        self.entries.pop(item_line_id, None)
        self.save()
        return True

    def load(self):
        self.entries = {entry['id']: ItemLine.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])
