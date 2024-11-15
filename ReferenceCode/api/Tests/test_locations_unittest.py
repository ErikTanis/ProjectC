import unittest
from unittest.mock import patch, MagicMock
from models.base import Base
from models.locations import Locations

class TestLocations(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {"id": 1, "warehouse_id": 1, "name": "Location A"},
            {"id": 2, "warehouse_id": 1, "name": "Location B"},
            {"id": 3, "warehouse_id": 2, "name": "Location C"},
        ]
        self.root_path = "/fake/path/"
        with patch('locations.LOCATIONS', self.test_data):
            self.locations = Locations(self.root_path, is_debug=True)

    def test_get_locations(self):
        self.assertEqual(self.locations.get_locations(), self.test_data)

    def test_get_location(self):
        location = self.locations.get_location(1)
        self.assertEqual(location, self.test_data[0])

    def test_get_location_not_found(self):
        location = self.locations.get_location(999)
        self.assertIsNone(location)

    def test_get_locations_in_warehouse(self):
        locations_in_warehouse = self.locations.get_locations_in_warehouse(1)
        self.assertEqual(locations_in_warehouse, self.test_data[:2])

    def test_add_location(self):
        new_location = {"id": 4, "warehouse_id": 3, "name": "Location D"}
        with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
            self.locations.add_location(new_location)
            self.assertIn(new_location, self.locations.get_locations())

    def test_update_location(self):
        updated_location = {"id": 1, "warehouse_id": 1, "name": "Updated Location"}
        with patch.object(Base, 'get_timestamp', return_value="2023-01-01"):
            self.locations.update_location(1, updated_location)
            self.assertEqual(self.locations.get_location(1), updated_location)

    def test_remove_location(self):
        self.locations.remove_location(1)
        self.assertIsNone(self.locations.get_location(1))

    @patch('builtins.open', new_callable=MagicMock)
    @patch('json.dump')
    def test_save(self, mock_json_dump, mock_open):
        self.locations.save()
        mock_open.assert_called_once_with(self.root_path + "locations.json", "w")
        mock_json_dump.assert_called_once_with(self.test_data, mock_open.return_value)

if __name__ == "__main__":
    unittest.main()
