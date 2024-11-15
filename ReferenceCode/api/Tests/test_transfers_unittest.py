import unittest
from unittest.mock import patch, MagicMock
from models.base import Base
from models.transfers import Transfers

class TestTransfers(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"id": 1, "items": ["item1", "item2"], "transfer_status": "Scheduled"},
            {"id": 2, "items": ["item3", "item4"], "transfer_status": "Completed"},
            {"id": 3, "items": ["item5"], "transfer_status": "Scheduled"},
        ]
        self.root_path = "/fake/path/"
        with patch('transfers.TRANSFERS', self.test_data):
            self.transfers = Transfers(self.root_path, is_debug=True)

    def test_get_transfers(self):
        self.assertEqual(self.transfers.get_transfers(), self.test_data)

    def test_get_transfer(self):
        transfer = self.transfers.get_transfer(1)
        self.assertEqual(transfer, self.test_data[0])

    def test_get_transfer_not_found(self):
        transfer = self.transfers.get_transfer(999)
        self.assertIsNone(transfer)

    def test_get_items_in_transfer(self):
        items = self.transfers.get_items_in_transfer(1)
        self.assertEqual(items, ["item1", "item2"])

    def test_get_items_in_transfer_not_found(self):
        items = self.transfers.get_items_in_transfer(999)
        self.assertIsNone(items)

    def test_add_transfer(self):
        new_transfer = {"id": 4, "items": ["item6", "item7"]}
        with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
            self.transfers.add_transfer(new_transfer)
            new_transfer["transfer_status"] = "Scheduled"
            self.assertIn(new_transfer, self.transfers.get_transfers())

    def test_update_transfer(self):
        updated_transfer = {"id": 1, "items": ["item1", "item2", "item3"], "transfer_status": "In Transit"}
        with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
            self.transfers.update_transfer(1, updated_transfer)
            self.assertEqual(self.transfers.get_transfer(1), updated_transfer)

    def test_remove_transfer(self):
        self.transfers.remove_transfer(1)
        self.assertIsNone(self.transfers.get_transfer(1))

    @patch('builtins.open', new_callable=MagicMock)
    @patch('json.dump')
    def test_save(self, mock_json_dump, mock_open):
        self.transfers.save()
        mock_open.assert_called_once_with(self.root_path + "transfers.json", "w")
        mock_json_dump.assert_called_once_with(self.test_data, mock_open.return_value)

if __name__ == "__main__":
    unittest.main()
