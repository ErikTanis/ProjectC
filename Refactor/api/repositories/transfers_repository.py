import json
from models.transfer import Transfer

class TransferRepository(BaseRepository):
    def __init__(self):
        super().__init__("transfers.json", False)
        self.load()

    def get_transfers(self):
        return self.transfers

    def get(self, transfer_id):
        for x in self.transfers:
            if x["id"] == transfer_id:
                return x
        return None

    def get_items_in_transfer(self, transfer_id):
        for x in self.transfers:
            if x["id"] == transfer_id:
                return x["items"]
        return None

    def add(self, transfer):
        transfer["transfer_status"] = "Scheduled"
        transfer["created_at"] = self.get_timestamp()
        transfer["updated_at"] = self.get_timestamp()
        self.transfers.append(transfer)
        self.save()

    def update(self, transfer_id, transfer):
        transfer["updated_at"] = self.get_timestamp()
        for i in range(len(self.transfers)):
            if self.transfers[i]["id"] == transfer_id:
                self.transfers[i] = transfer
                break
        self.save()

    def remove(self, transfer_id):
        for x in self.transfers:
            if x["id"] == transfer_id:
                self.transfers.remove(x)
        self.save()

    def load(self):
        data = super().load()
        self.transfers = []
        for x in data:
            self.transfers.append(Transfer(**x))

    def save(self):
        data = []
        for x in self.transfers:
            data.append(x.__dict__)
        super().save(data)