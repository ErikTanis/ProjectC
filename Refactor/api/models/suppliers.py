from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Supplier:
    id: int
    code: str
    name: str
    address: str
    address_extra: str
    city: str
    zip_code: str
    province: str
    country: str
    contact_name: str
    phonenumber: str
    reference: str
    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    updated_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat() + "Z")

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

        return Supplier(
            id=data['id'],
            code=data['code'],
            name=data['name'],
            address=data['address'],
            address_extra=data['address_extra'],
            city=data['city'],
            zip_code=data['zip_code'],
            province=data['province'],
            country=data['country'],
            contact_name=data['contact_name'],
            phonenumber=data['phonenumber'],
            reference=data['reference'],
            created_at=created_at,
            updated_at=updated_at
        )
