from api.providers import repository_provider
from Base_controller import BaseController
from api.models.transfer import Transfer

class TransfersController(BaseController):
    def __init__(self):
        self.provider = repository_provider

    def handle_get_version_1(self, path, handler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                transfer_id = int(path[1])
                self.get_by_id(handler, transfer_id)
            case _:
                self.respond_not_found(handler)

    def handle_post_version_1(self, handler):
        self.add(handler)

    def handle_put_version_1(self, path, handler):
        transfer_id = int(path[1])
        self.update(handler, transfer_id)

    def handle_delete_version_1(self, path, handler):
        transfer_id = int(path[1])
        self.delete(handler, transfer_id)

    # /api/v1/transfers
    def get_all(self, handler):
        transfers = self.provider.fetch_transfer_pool().get_transfers()
        self.respond_ok(handler, transfers)

    # /api/v1/transfers/{transfer_id}
    def get_by_id(self, handler, transfer_id):
        transfer = self.provider.fetch_transfer_pool().get(transfer_id)
        self.respond_ok(handler, transfer)

    # /api/v1/transfers
    def add(self, handler):
        content = self.get_json_body(handler)
        transfer = Transfer.from_dict(content)
        self.provider.fetch_transfer_pool().add(transfer)
        self.respond_ok(handler, transfer)

    # /api/v1/transfers/{transfer_id}
    def update(self, handler, transfer_id):
        content = self.get_json_body(handler)
        transfer = Transfer.from_dict(content)
        self.provider.fetch_transfer_pool().update(transfer_id, transfer)
        self.respond_ok(handler, transfer)

    # /api/v1/transfers/{transfer_id}
    def delete(self, handler, transfer_id):
        self.provider.fetch_transfer_pool().remove(transfer_id)
        self.respond_ok(handler, None)