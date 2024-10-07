from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Order:
    id: int
    source_id: int
    order_date: datetime
    request_date: datetime
    reference: str
    reference_extra: str
    order_status: str
    notes: str
    shipping_notes: str
    picking_notes: str
    warehouse_id: int
    ship_to: str
    bill_to: str
    shipment_id: int
    total_amount: float
    total_discount: float
    total_tax: float
    total_surcharge: float
    created_at: datetime
    updated_at: datetime
    items: list

    @staticmethod
    def from_dict(data: dict):
        created_at = data.get(
            'created_at', datetime.utcnow().isoformat() + "Z")
        updated_at = data.get(
            'updated_at', datetime.utcnow().isoformat() + "Z")

        if not created_at.endswith("Z"):
            created_at = datetime.strptime(
                created_at, "%Y-%m-%d %H:%M:%S").isoformat() + "Z"
        if not updated_at.endswith("Z"):
            updated_at = datetime.strptime(
                updated_at, "%Y-%m-%d %H:%M:%S").isoformat() + "Z"

        return Order(
            id=data['id'],
            source_id=data['source_id'],
            order_date=data['order_date'],
            request_date=data['request_date'],
            reference=data['reference'],
            reference_extra=data['reference_extra'],
            order_status=data['order_status'],
            notes=data['notes'],
            shipping_notes=data['shipping_notes'],
            picking_notes=data['picking_notes'],
            warehouse_id=data['warehouse_id'],
            ship_to=data['ship_to'],
            bill_to=data['bill_to'],
            shipment_id=data['shipment_id'],
            total_amount=data['total_amount'],
            total_discount=data['total_discount'],
            total_tax=data['total_tax'],
            total_surcharge=data['total_surcharge'],
            created_at=created_at,
            updated_at=updated_at,
            items=data['items']
        )