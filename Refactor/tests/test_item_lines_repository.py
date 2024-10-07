import pytest
from api.models.item_lines import ItemLine
from api.repositories.item_lines_repository import ItemLinesRepository
from datetime import datetime, timezone
from faker import Faker
import random

fake = Faker()

@pytest.fixture
def item_lines_repository():
    return ItemLinesRepository(is_debug=True)

@pytest.fixture
def random_item_line():
    return generate_random_item_line()

def generate_random_item_line(id=None) -> ItemLine:
    return ItemLine(
        id=id if id is not None else random.randint(1, 1000),
        name=fake.word(),
        description=fake.sentence(),
        created_at=fake.date_time_this_decade(tzinfo=timezone.utc).isoformat(),
        updated_at=datetime.now(timezone.utc).isoformat()
    )

def test_get_all(item_lines_repository):
    for _ in range(5):
        item_lines_repository.add(generate_random_item_line())
    
    all_item_lines = item_lines_repository.get_all()
    assert len(all_item_lines) == 5

def test_get_by_id(item_lines_repository):
    random_item_line = generate_random_item_line(id=1)
    item_lines_repository.add(random_item_line)
    item_line = item_lines_repository.get_by_id(1)
    
    assert item_line is not None
    assert item_line.id == 1

def test_get_by_id_non_existing(item_lines_repository):
    item_line = item_lines_repository.get_by_id(999)
    assert item_line is None

def test_add_item_line(item_lines_repository, random_item_line):
    result = item_lines_repository.add(random_item_line)
    result_item = item_lines_repository.get_by_id(random_item_line.id)
    
    assert result_item is not None
    assert result == True

def test_add_item_line_existing(item_lines_repository, random_item_line):
    result = item_lines_repository.add(random_item_line)
    result_duplicate = item_lines_repository.add(random_item_line)
    result_item = item_lines_repository.get_by_id(random_item_line.id)
    
    assert result_item is not None
    assert result == True
    assert result_duplicate == False

def test_update_item_line(item_lines_repository, random_item_line):
    item_lines_repository.add(random_item_line)
    
    updated_item_line = random_item_line
    updated_item_line.name = "Updated Name"
    item_lines_repository.update(random_item_line.id, updated_item_line)
    
    result = item_lines_repository.get_by_id(random_item_line.id)
    assert result.name == "Updated Name"

def test_update_item_line_non_existing(item_lines_repository, random_item_line):
    updated_item_line = random_item_line
    updated_item_line.name = "Updated Name"
    result = item_lines_repository.update(random_item_line.id, updated_item_line)
    result_get = item_lines_repository.get_by_id(random_item_line.id)
    
    assert result == False
    assert result_get is None

def test_remove_item_line(item_lines_repository, random_item_line):
    item_lines_repository.add(random_item_line)
    item_lines_repository.remove(random_item_line.id)
    
    assert item_lines_repository.get_by_id(random_item_line.id) is None

def test_remove_item_line_non_existing(item_lines_repository, random_item_line):
    result = item_lines_repository.remove(random_item_line.id)
    result_get = item_lines_repository.get_by_id(random_item_line.id)

    assert result_get is None
    assert result == False
