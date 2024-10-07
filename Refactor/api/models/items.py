from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Item:
    uid: str
    code: str
    description: str
    short_description: str
    upc_code: str
    model_number: str
    commodity_code: str
    item_line: int
    item_group: int
    item_type: int
    unit_purchase_quantity: int
    unit_order_quantity: int
    pack_order_quantity: int
    supplier_id: int
    supplier_code: str
    supplier_part_number: str
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

    @staticmethod
    def from_dict(data: dict):
        created_at = data.get('created_at', datetime.utcnow().isoformat() + "Z")
        updated_at = data.get('updated_at', datetime.utcnow().isoformat() + "Z")

        if not created_at.endswith("Z"):
            created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S").isoformat() + "Z"
        if not updated_at.endswith("Z"):
            updated_at = datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S").isoformat() + "Z"

        return Item(
            uid=data['uid'],
            code=data['code'],
            description=data['description'],
            short_description=data['short_description'],
            upc_code=data['upc_code'],
            model_number=data['model_number'],
            commodity_code=data['commodity_code'],
            item_line=data['item_line'],
            item_group=data['item_group'],
            item_type=data['item_type'],
            unit_purchase_quantity=data['unit_purchase_quantity'],
            unit_order_quantity=data['unit_order_quantity'],
            pack_order_quantity=data['pack_order_quantity'],
            supplier_id=data['supplier_id'],
            supplier_code=data['supplier_code'],
            supplier_part_number=data['supplier_part_number'],
            created_at=created_at,
            updated_at=updated_at
        )
    