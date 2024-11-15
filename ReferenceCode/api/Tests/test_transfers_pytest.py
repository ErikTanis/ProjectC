import pytest
from unittest.mock import patch, MagicMock
from models.base import Base
from models.transfers import Transfers

@pytest.fixture
def test_data():
    return [
        {"id": 1, "items": ["item1", "item2"], "transfer_status": "Scheduled"},
        {"id": 2, "items": ["item3", "item4"], "transfer_status": "Completed"},
        {"id": 3, "items": ["item5"], "transfer_status": "Scheduled"},
    ]

@pytest.fixture
def transfers(test_data):
    with patch('transfers.TRANSFERS', test_data):
        return Transfers("/fake/path/", is_debug=True)

def test_get_transfers(transfers, test_data):
    assert transfers.get_transfers() == test_data

def test_get_transfer(transfers, test_data):
    assert transfers.get_transfer(1) == test_data[0]

def test_get_transfer_not_found(transfers):
    assert transfers.get_transfer(999) is None

def test_get_items_in_transfer(transfers):
    assert transfers.get_items_in_transfer(1) == ["item1", "item2"]

def test_get_items_in_transfer_not_found(transfers):
    assert transfers.get_items_in_transfer(999) is None

def test_add_transfer(transfers):
    new_transfer = {"id": 4, "items": ["item6", "item7"]}
    with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
        transfers.add_transfer(new_transfer)
        new_transfer["transfer_status"] = "Scheduled"
        assert new_transfer in transfers.get_transfers()

def test_update_transfer(transfers):
    updated_transfer = {"id": 1, "items": ["item1", "item2", "item3"], "transfer_status": "In Transit"}
    with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
        transfers.update_transfer(1, updated_transfer)
        assert transfers.get_transfer(1) == updated_transfer

def test_remove_transfer(transfers):
    transfers.remove_transfer(1)
    assert transfers.get_transfer(1) is None

def test_save(transfers, test_data):
    with patch("builtins.open", new_callable=MagicMock) as mock_open, patch("json.dump") as mock_json_dump:
        transfers.save()
        mock_open.assert_called_once_with("/fake/path/transfers.json", "w")
        mock_json_dump.assert_called_once_with(test_data, mock_open.return_value)
