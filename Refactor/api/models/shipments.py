from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Shipment:
    id: int
    order_id: int
    source_id: int
    order_date: str = field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d"))
    request_date: str = field(
        default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d"))
    shipment_date: str = field(
        default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d"))
    shipment_type: str
    shipment_status: str
    notes: str
    carrier_code: str
    carrier_description: str
    service_code: str
    payment_type: str
    transfer_mode: str
    total_package_count: int
    total_package_weight: float
    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    updated_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat() + "Z")
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

        return Shipment(
            id=data['id'],
            order_id=data['order_id'],
            source_id=data['source_id'],
            order_date=data['order_date'],
            request_date=data['request_date'],
            shipment_date=data['shipment_date'],
            shipment_type=data['shipment_type'],
            shipment_status=data['shipment_status'],
            notes=data['notes'],
            carrier_code=data['carrier_code'],
            carrier_description=data['carrier_description'],
            service_code=data['service_code'],
            payment_type=data['payment_type'],
            transfer_mode=data['transfer_mode'],
            total_package_count=data['total_package_count'],
            total_package_weight=data['total_package_weight'],
            created_at=created_at,
            updated_at=updated_at,
            items=data['items']
        )
