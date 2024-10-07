from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class ItemGroup:
    id: int
    name: str
    description: str
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

        return ItemGroup(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            created_at=created_at,
            updated_at=updated_at
        )
