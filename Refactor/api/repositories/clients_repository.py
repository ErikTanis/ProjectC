from Refactor.api.providers import repository_provider
from repositories.base_repository import BaseRepository
from models.clients import Client

JSON_FILE_NAME = "clients.json"


class ClientsRepository(BaseRepository):
    def __init__(self, root_path=None, is_debug=False):
        super().__init__(JSON_FILE_NAME, root_path, is_debug)
        self.load()

    def load(self):
        self.entries = {entry['id']: Client.from_dict(
            entry) for entry in super().load()}

    def save(self):
        super().save([entry.__dict__ for entry in self.entries.values()])

    def get_clients(self):
        return list(self.entries.values())

    def get_client(self, client_id):
        if client_id in self.entries:
            return self.entries[client_id]
        return None

    def add_client(self, client):
        client["created_at"] = self.get_timestamp()
        client["updated_at"] = self.get_timestamp()
        self.entries[client.id] = client

    def update_client(self, client_id, client):
        client["updated_at"] = self.get_timestamp()
        if client_id in self.entries:
            self.entries[client_id] = client

    def remove_client(self, client_id):
        if client_id in self.entries:
            del self.entries[client_id]
