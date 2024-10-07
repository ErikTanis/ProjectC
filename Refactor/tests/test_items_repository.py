import pytest
from api.models.items import Item
from api.repositories.items_repository import ItemsRepository
from datetime import datetime, timezone
from uuid import uuid4
from faker import Faker
import random

fake = Faker()

@pytest.fixture
def items_repository():
    return ItemsRepository(is_debug=True)

@pytest.fixture
def random_item():
    return generate_random_item()

def generate_random_item(
    uid=None,
    item_line=None,
    item_group=None,
    item_type=None,
    supplier_id=None
) -> Item:
    return Item(
        uid=uid if uid is not None else str(uuid4()),
        code=fake.bothify(text='???#####'),
        description=fake.catch_phrase(),
        short_description=fake.word(),
        upc_code=fake.ean13(),
        model_number=fake.bothify(text='##-???###'),
        commodity_code=fake.bothify(text='???###'),
        item_line=item_line if item_line is not None else random.randint(1, 100),
        item_group=item_group if item_group is not None else random.randint(1, 100),
        item_type=item_type if item_type is not None else random.randint(1, 50),
        unit_purchase_quantity=random.randint(1, 100),
        unit_order_quantity=random.randint(1, 100),
        pack_order_quantity=random.randint(1, 50),
        supplier_id=supplier_id if supplier_id is not None else random.randint(1, 50),
        supplier_code=fake.bothify(text='SUP###'),
        supplier_part_number=fake.bothify(text='???-#####'),
        created_at=fake.date_time_this_decade(tzinfo=timezone.utc).isoformat(),
        updated_at=datetime.now(timezone.utc).isoformat()
    )

def test_get_all(items_repository):
    for _ in range(5):
        items_repository.add(generate_random_item())
    
    all_items = items_repository.get_all()
    assert len(all_items) == 5

def test_get_all_by_item_line(items_repository):
    item_line_id = 101
    for _ in range(3):
        random_item = generate_random_item(item_line= item_line_id)
        items_repository.add(random_item)

    results = items_repository.get_all_by_item_line(item_line_id)
    assert len(results) == 3
    assert all(item.item_line == item_line_id for item in results)

def test_get_all_by_item_group(items_repository):
    item_group = 102
    for _ in range(3):
        random_item = generate_random_item(item_group= item_group)
        items_repository.add(random_item)

    results = items_repository.get_all_by_item_group(item_group)
    assert len(results) == 3
    assert all(item.item_group == item_group for item in results)

def test_get_all_by_item_type(items_repository):
    item_type = 103
    for _ in range(3):
        random_item = generate_random_item(item_type= item_type)
        items_repository.add(random_item)

    results = items_repository.get_all_by_item_type(item_type)
    assert len(results) == 3
    assert all(item.item_type == item_type for item in results)

def test_get_all_by_supplier(items_repository):
    supplier = 104
    for _ in range(3):
        random_item = generate_random_item(supplier_id= supplier)
        items_repository.add(random_item)

    results = items_repository.get_all_by_supplier(supplier)
    assert len(results) == 3
    assert all(item.supplier_id == supplier for item in results)

def test_get_by_id(items_repository, random_item):
    items_repository.add(random_item)
    item = items_repository.get_by_id(random_item.uid)
    
    assert item is not None
    assert item.uid == random_item.uid

def test_get_by_id_non_existing(items_repository, random_item):
    items_repository.add(random_item)
    item = items_repository.get_by_id("1")
    
    assert item is None

def test_add_item(items_repository, random_item):
    result = items_repository.add(random_item)
    result_item = items_repository.get_by_id(random_item.uid)
    
    assert result_item is not None
    assert result == True

def test_add_item_existing(items_repository, random_item):
    result = items_repository.add(random_item)
    result_duplicate = items_repository.add(random_item)
    result_item = items_repository.get_by_id(random_item.uid)
    
    assert result_item is not None
    assert result == True
    assert result_duplicate == False

def test_update_item(items_repository, random_item):
    items_repository.add(random_item)
    
    updated_item = random_item
    updated_item.description = "Updated description"
    items_repository.update(random_item.uid, updated_item)
    
    result = items_repository.get_by_id(random_item.uid)
    assert result.description == "Updated description"

def test_update_item_non_existing(items_repository, random_item):
    updated_item = random_item
    updated_item.description = "Updated description"
    result = items_repository.update(random_item.uid, updated_item)
    result_get = items_repository.get_by_id(random_item.uid)
    
    assert result == False
    assert result_get is None

def test_remove_item(items_repository, random_item):
    items_repository.add(random_item)
    items_repository.remove(random_item.uid)
    
    assert items_repository.get_by_id(random_item.uid) is None

def test_remove_item_non_existing(items_repository, random_item):
    result = items_repository.remove(random_item.uid)
    result_get = items_repository.get_by_id(random_item.uid)

    assert result_get is None
    assert result == False