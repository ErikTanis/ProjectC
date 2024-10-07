import pytest
from datetime import datetime, timezone
from faker import Faker
import random
from api.models.item_types import ItemType
from api.repositories.item_types_repository import ItemTypesRepository
import json

fake = Faker()

@pytest.fixture
def item_types_repository():
    return ItemTypesRepository(is_debug=True)

@pytest.fixture
def random_item_type():
    return generate_random_item_type()

def generate_random_item_type(id=None) -> ItemType:
    return ItemType(
        id=id if id is not None else random.randint(1, 1000),
        name=fake.word(),
        description=fake.sentence(),
        created_at=fake.date_time_this_decade(tzinfo=timezone.utc).isoformat(),
        updated_at=datetime.now(timezone.utc).isoformat()
    )

def test_get_all(item_types_repository):
    for _ in range(5):
        item_types_repository.add(generate_random_item_type())
    
    all_item_types = item_types_repository.get_all()

    assert len(all_item_types) == 5

def test_get_by_id(item_types_repository):
    random_item_type = generate_random_item_type(id=1)
    item_types_repository.add(random_item_type)
    item_type = item_types_repository.get_by_id(1)
    
    assert item_type is not None
    assert item_type.id == 1

def test_get_by_id_non_existing(item_types_repository):
    item_type = item_types_repository.get_by_id(999)
    assert item_type is None

def test_add_item_type(item_types_repository, random_item_type):
    result = item_types_repository.add(random_item_type)
    result_item = item_types_repository.get_by_id(random_item_type.id)
    
    assert result_item is not None
    assert result == True

def test_add_item_type_existing(item_types_repository, random_item_type):
    result = item_types_repository.add(random_item_type)
    result_duplicate = item_types_repository.add(random_item_type)
    result_item = item_types_repository.get_by_id(random_item_type.id)
    
    assert result_item is not None
    assert result == True
    assert result_duplicate == False

def test_update_item_type(item_types_repository, random_item_type):
    item_types_repository.add(random_item_type)
    
    updated_item_type = random_item_type
    updated_item_type.name = "Updated Name"
    item_types_repository.update(random_item_type.id, updated_item_type)
    
    result = item_types_repository.get_by_id(random_item_type.id)
    assert result.name == "Updated Name"

def test_update_item_type_non_existing(item_types_repository, random_item_type):
    updated_item_type = random_item_type
    updated_item_type.name = "Updated Name"
    result = item_types_repository.update(random_item_type.id, updated_item_type)
    result_get = item_types_repository.get_by_id(random_item_type.id)
    
    assert result == False
    assert result_get is None

def test_remove_item_type(item_types_repository, random_item_type):
    item_types_repository.add(random_item_type)
    item_types_repository.remove(random_item_type.id)
    
    assert item_types_repository.get_by_id(random_item_type.id) is None

def test_remove_item_type_non_existing(item_types_repository, random_item_type):
    result = item_types_repository.remove(random_item_type.id)
    result_get = item_types_repository.get_by_id(random_item_type.id)

    assert result_get is None
    assert result == False
