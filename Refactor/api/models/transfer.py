class Transfer:
    def __init__(self, reference, transfer_from, transfer_to, transfer_status, created_at, updated_at):
        self.reference = reference
        self.transfer_from = transfer_from
        self.transfer_to = transfer_to
        self.transfer_status = transfer_status
        self.created_at = created_at
        self.updated_at = updated_at

class TransferItem:
    def __init__(self, item_id, amount):
        self.item_id = item_id
        self.amount = amount