import unittest
from unittest.mock import patch, MagicMock
from models.base import Base
from models.warehouses import Warehouses

class TestWarehouses(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"id": 1, "name": "Warehouse A", "location": "City A"},
            {"id": 2, "name": "Warehouse B", "location": "City B"},
            {"id": 3, "name": "Warehouse C", "location": "City C"},
        ]
        self.root_path = "/fake/path/"
        with patch('warehouses.WAREHOUSES', self.test_data):
            self.warehouses = Warehouses(self.root_path, is_debug=True)

    def test_get_warehouses(self):
        self.assertEqual(self.warehouses.get_warehouses(), self.test_data)

    def test_get_warehouse(self):
        warehouse = self.warehouses.get_warehouse(1)
        self.assertEqual(warehouse, self.test_data[0])

    def test_get_warehouse_not_found(self):
        warehouse = self.warehouses.get_warehouse(999)
        self.assertIsNone(warehouse)

    def test_add_warehouse(self):
        new_warehouse = {"id": 4, "name": "Warehouse D", "location": "City D"}
        with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
            self.warehouses.add_warehouse(new_warehouse)
            self.assertIn(new_warehouse, self.warehouses.get_warehouses())

    def test_update_warehouse(self):
        updated_warehouse = {"id": 1, "name": "Updated Warehouse A", "location": "City A"}
        with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
            self.warehouses.update_warehouse(1, updated_warehouse)
            self.assertEqual(self.warehouses.get_warehouse(1), updated_warehouse)

    def test_remove_warehouse(self):
        self.warehouses.remove_warehouse(1)
        self.assertIsNone(self.warehouses.get_warehouse(1))

    @patch('builtins.open', new_callable=MagicMock)
    @patch('json.dump')
    def test_save(self, mock_json_dump, mock_open):
        self.warehouses.save()
        mock_open.assert_called_once_with(self.root_path + "warehouses.json", "w")
        mock_json_dump.assert_called_once_with(self.test_data, mock_open.return_value)

if __name__ == "__main__":
    unittest.main()
