from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Inventory:
    id: int
    item_id: str
    description: str
    item_reference: str
    locations: List[int]
    total_on_hand: int
    total_expected: int
    total_ordered: int
    total_allocated: int
    total_available: int
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

        return Inventory(
            id=data['id'],
            item_id=data['item_id'],
            description=data['description'],
            item_reference=data['item_reference'],
            locations=data['locations'],
            total_on_hand=data['total_on_hand'],
            total_expected=data['total_expected'],
            total_ordered=data['total_ordered'],
            total_allocated=data['total_allocated'],
            total_available=data['total_available'],
            created_at=created_at,
            updated_at=updated_at
        )
