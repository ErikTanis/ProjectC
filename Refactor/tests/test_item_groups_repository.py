import pytest
from api.models.item_groups import ItemGroup
from api.repositories.item_groups_repository import ItemGroupsRepository
from datetime import datetime, timezone
from faker import Faker
import random

fake = Faker()

@pytest.fixture
def item_groups_repository():
    return ItemGroupsRepository(is_debug=True)

@pytest.fixture
def random_item_group():
    return generate_random_item_group()

def generate_random_item_group(id=None) -> ItemGroup:
    return ItemGroup(
        id=id if id is not None else random.randint(1, 1000),
        name=fake.word(),
        description=fake.sentence(),
        created_at=fake.date_time_this_decade(tzinfo=timezone.utc).isoformat(),
        updated_at=datetime.now(timezone.utc).isoformat()
    )

def test_get_all(item_groups_repository):
    for _ in range(5):
        item_groups_repository.add(generate_random_item_group())
    
    all_item_groups = item_groups_repository.get_all()
    assert len(all_item_groups) == 5

def test_get_by_id(item_groups_repository):
    random_item_group = generate_random_item_group(id=1)
    item_groups_repository.add(random_item_group)
    item_group = item_groups_repository.get_by_id(1)
    
    assert item_group is not None
    assert item_group.id == 1

def test_get_by_id_non_existing(item_groups_repository):
    item_group = item_groups_repository.get_by_id(999)
    assert item_group is None

def test_add_item_group(item_groups_repository, random_item_group):
    result = item_groups_repository.add(random_item_group)
    result_item = item_groups_repository.get_by_id(random_item_group.id)
    
    assert result_item is not None
    assert result == True

def test_add_item_group_existing(item_groups_repository, random_item_group):
    result = item_groups_repository.add(random_item_group)
    result_duplicate = item_groups_repository.add(random_item_group)
    result_item = item_groups_repository.get_by_id(random_item_group.id)
    
    assert result_item is not None
    assert result == True
    assert result_duplicate == False

def test_update_item_group(item_groups_repository, random_item_group):
    item_groups_repository.add(random_item_group)
    
    updated_item_group = random_item_group
    updated_item_group.name = "Updated Name"
    item_groups_repository.update(random_item_group.id, updated_item_group)
    
    result = item_groups_repository.get_by_id(random_item_group.id)
    assert result.name == "Updated Name"

def test_update_item_group_non_existing(item_groups_repository, random_item_group):
    updated_item_group = random_item_group
    updated_item_group.name = "Updated Name"
    result = item_groups_repository.update(random_item_group.id, updated_item_group)
    result_get = item_groups_repository.get_by_id(random_item_group.id)
    
    assert result == False
    assert result_get is None

def test_remove_item_group(item_groups_repository, random_item_group):
    item_groups_repository.add(random_item_group)
    item_groups_repository.remove(random_item_group.id)
    
    assert item_groups_repository.get_by_id(random_item_group.id) is None

def test_remove_item_group_non_existing(item_groups_repository, random_item_group):
    result = item_groups_repository.remove(random_item_group.id)
    result_get = item_groups_repository.get_by_id(random_item_group.id)

    assert result_get is None
    assert result == False
