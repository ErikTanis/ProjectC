import pytest
from unittest.mock import patch, MagicMock
from models.base import Base
from models.warehouses import Warehouses

@pytest.fixture
def test_data():
    return [
        {"id": 1, "name": "Warehouse A", "location": "City A"},
        {"id": 2, "name": "Warehouse B", "location": "City B"},
        {"id": 3, "name": "Warehouse C", "location": "City C"},
    ]

@pytest.fixture
def warehouses(test_data):
    with patch('warehouses.WAREHOUSES', test_data):
        return Warehouses("/fake/path/", is_debug=True)

def test_get_warehouses(warehouses, test_data):
    assert warehouses.get_warehouses() == test_data

def test_get_warehouse(warehouses, test_data):
    assert warehouses.get_warehouse(1) == test_data[0]

def test_get_warehouse_not_found(warehouses):
    assert warehouses.get_warehouse(999) is None

def test_add_warehouse(warehouses):
    new_warehouse = {"id": 4, "name": "Warehouse D", "location": "City D"}
    with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
        warehouses.add_warehouse(new_warehouse)
        assert new_warehouse in warehouses.get_warehouses()

def test_update_warehouse(warehouses):
    updated_warehouse = {"id": 1, "name": "Updated Warehouse A", "location": "City A"}
    with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
        warehouses.update_warehouse(1, updated_warehouse)
        assert warehouses.get_warehouse(1) == updated_warehouse

def test_remove_warehouse(warehouses):
    warehouses.remove_warehouse(1)
    assert warehouses.get_warehouse(1) is None

def test_save(warehouses, test_data):
    with patch("builtins.open", new_callable=MagicMock) as mock_open, patch("json.dump") as mock_json_dump:
        warehouses.save()
        mock_open.assert_called_once_with("/fake/path/warehouses.json", "w")
        mock_json_dump.assert_called_once_with(test_data, mock_open.return_value)
