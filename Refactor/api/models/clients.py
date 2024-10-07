from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Client:
    id: int
    name: str
    address: str
    city: str
    zip_code: str
    province: str
    country: str
    contact_name: str
    contact_phone: str
    contact_email: str
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

        return Client(
            id=data['id'],
            name=data['name'],
            address=data['address'],
            city=data['city'],
            zip_code=data['zip_code'],
            province=data['province'],
            country=data['country'],
            contact_name=data['contact_name'],
            contact_phone=data['contact_phone'],
            contact_email=data['contact_email'],
            created_at=created_at,
            updated_at=updated_at
        )
