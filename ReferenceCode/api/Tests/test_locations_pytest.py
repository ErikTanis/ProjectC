import pytest
from unittest.mock import patch, MagicMock
from models.base import Base
from models.locations import Locations

@pytest.fixture
def test_data():
    return [
        {"id": 1, "warehouse_id": 1, "name": "Location A"},
        {"id": 2, "warehouse_id": 1, "name": "Location B"},
        {"id": 3, "warehouse_id": 2, "name": "Location C"},
    ]

@pytest.fixture
def locations(test_data):
    with patch('locations.LOCATIONS', test_data):
        return Locations("/fake/path/", is_debug=True)

def test_get_locations(locations, test_data):
    assert locations.get_locations() == test_data

def test_get_location(locations, test_data):
    assert locations.get_location(1) == test_data[0]

def test_get_location_not_found(locations):
    assert locations.get_location(999) is None

def test_get_locations_in_warehouse(locations, test_data):
    assert locations.get_locations_in_warehouse(1) == test_data[:2]

def test_add_location(locations):
    new_location = {"id": 4, "warehouse_id": 3, "name": "Location D"}
    with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
        locations.add_location(new_location)
        assert new_location in locations.get_locations()

def test_update_location(locations):
    updated_location = {"id": 1, "warehouse_id": 1, "name": "Updated Location"}
    with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
        locations.update_location(1, updated_location)
        assert locations.get_location(1) == updated_location

def test_remove_location(locations):
    locations.remove_location(1)
    assert locations.get_location(1) is None

def test_save(locations, test_data):
    with patch("builtins.open", new_callable=MagicMock) as mock_open, patch("json.dump") as mock_json_dump:
        locations.save()
        mock_open.assert_called_once_with("/fake/path/locations.json", "w")
        mock_json_dump.assert_called_once_with(test_data, mock_open.return_value)
