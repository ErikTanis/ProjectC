import pytest
from api.models.inventories import Inventory
from api.repositories.inventories_repository import InventoriesRepository
from datetime import datetime, timezone
from faker import Faker
import random

fake = Faker()

@pytest.fixture
def inventories_repository():
    return InventoriesRepository(is_debug=True)

@pytest.fixture
def random_inventory():
    return generate_random_inventory()

def generate_random_inventory(id=None, item_id=None) -> Inventory:
    return Inventory(
        id=id if id is not None else random.randint(1, 1000),
        item_id=item_id if item_id is not None else str(random.randint(1, 1000)),
        description=fake.sentence(),
        item_reference=fake.word(),
        locations=[random.randint(1000, 9999) for _ in range(3)],
        total_on_hand=random.randint(1, 1000),
        total_expected=random.randint(1, 100),
        total_ordered=random.randint(1, 100),
        total_allocated=random.randint(1, 100),
        total_available=random.randint(1, 100),
        created_at=fake.date_time_this_decade(tzinfo=timezone.utc).isoformat(),
        updated_at=datetime.now(timezone.utc).isoformat()
    )

def test_get_all(inventories_repository):
    for _ in range(5):
        inventories_repository.add(generate_random_inventory())
    
    all_inventories = inventories_repository.get_all()
    assert len(all_inventories) == 5

def test_get_by_id(inventories_repository):
    random_inventory = generate_random_inventory(id=1)
    inventories_repository.add(random_inventory)
    inventory = inventories_repository.get_by_id(1)
    
    assert inventory is not None
    assert inventory.id == 1

def test_get_by_id_non_existing(inventories_repository):
    inventory = inventories_repository.get_by_id(999)
    assert inventory is None

def test_add_inventory(inventories_repository, random_inventory):
    result = inventories_repository.add(random_inventory)
    result_item = inventories_repository.get_by_id(random_inventory.id)
    
    assert result_item is not None
    assert result == True

def test_add_inventory_existing(inventories_repository, random_inventory):
    result = inventories_repository.add(random_inventory)
    result_duplicate = inventories_repository.add(random_inventory)
    result_item = inventories_repository.get_by_id(random_inventory.id)
    
    assert result_item is not None
    assert result == True
    assert result_duplicate == False

def test_update_inventory(inventories_repository, random_inventory):
    inventories_repository.add(random_inventory)
    
    updated_inventory = random_inventory
    updated_inventory.description = "Updated description"
    inventories_repository.update(random_inventory.id, updated_inventory)
    
    result = inventories_repository.get_by_id(random_inventory.id)
    assert result.description == "Updated description"

def test_update_inventory_non_existing(inventories_repository, random_inventory):
    updated_inventory = random_inventory
    updated_inventory.description = "Updated description"
    result = inventories_repository.update(random_inventory.id, updated_inventory)
    result_get = inventories_repository.get_by_id(random_inventory.id)
    
    assert result == False
    assert result_get is None

def test_remove_inventory(inventories_repository, random_inventory):
    inventories_repository.add(random_inventory)
    inventories_repository.remove(random_inventory.id)
    
    assert inventories_repository.get_by_id(random_inventory.id) is None

def test_remove_inventory_non_existing(inventories_repository, random_inventory):
    result = inventories_repository.remove(random_inventory.id)
    result_get = inventories_repository.get_by_id(random_inventory.id)

    assert result_get is None
    assert result == False

def test_get_all_by_item_id(inventories_repository):
    item_id = "item_001"
    for _ in range(3):
        random_inventory = generate_random_inventory(item_id=item_id)
        inventories_repository.add(random_inventory)

    results = inventories_repository.get_all_by_item_id(item_id)
    assert len(results) == 3
    assert all(inventory.item_id == item_id for inventory in results)

def test_get_totals_by_item_id(inventories_repository):
    item_id = "item_001"
    inventories = [
        generate_random_inventory(item_id=item_id, id=1),
        generate_random_inventory(item_id=item_id, id=2),
        generate_random_inventory(item_id=item_id, id=3),
    ]
    
    for inventory in inventories:
        inventories_repository.add(inventory)

    totals = inventories_repository.get_totals_by_item_id(item_id)
    
    expected_totals = {
        "total_expected": sum(inventory.total_expected for inventory in inventories),
        "total_ordered": sum(inventory.total_ordered for inventory in inventories),
        "total_allocated": sum(inventory.total_allocated for inventory in inventories),
        "total_available": sum(inventory.total_available for inventory in inventories),
    }

    assert totals == expected_totals
