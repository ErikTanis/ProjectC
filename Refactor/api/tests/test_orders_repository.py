import unittest
import json
from datetime import datetime
from unittest.mock import MagicMock, patch
from controllers.orders_controller import OrdersController
from models.orders import Order
from models.items import Item

class MockHandler:
    def __init__(self):
        self.response_code = None
        self.headers = {}
        self.response_data = None
        self.written_data = None

    def send_response(self, code):
        self.response_code = code

    def send_header(self, key, value):
        self.headers[key] = value

    def end_headers(self):
        pass

    def wfile(self):
        return self

    def write(self, data):
        self.written_data = data

class TestOrdersController(unittest.TestCase):
    def setUp(self):
        self.controller = OrdersController()
        self.handler = MockHandler()
        self.sample_order = Order(
            id=1,
            source_id=1,
            order_date=datetime.now().isoformat(),
            request_date=datetime.now().isoformat(),
            reference="TEST-REF",
            reference_extra="",
            order_status="Pending",
            notes="",
            shipping_notes="",
            picking_notes="",
            warehouse_id=1,
            ship_to="Test Address",
            bill_to="Test Billing",
            shipment_id=1,
            total_amount=100.0,
            total_discount=0.0,
            total_tax=0.0,
            total_surcharge=0.0,
            created_at=datetime.now().isoformat() + "Z",
            updated_at=datetime.now().isoformat() + "Z",
            items=[]
        )

    @patch('providers.repository_provider.fetch_order_pool')
    def test_get_all_orders(self, mock_repo):
        # Setup
        mock_repo.return_value.get_orders.return_value = [self.sample_order]
        
        # Execute
        self.controller.get_all(self.handler)
        
        # Assert
        self.assertEqual(self.handler.response_code, 200)
        self.assertEqual(self.handler.headers.get("Content-Type"), "application/json")

    @patch('providers.repository_provider.fetch_order_pool')
    def test_get_order_by_id(self, mock_repo):
        # Setup
        mock_repo.return_value.get_order.return_value = self.sample_order
        
        # Execute
        self.controller.get_by_id(self.handler, 1)
        
        # Assert
        self.assertEqual(self.handler.response_code, 200)
        self.assertEqual(self.handler.headers.get("Content-Type"), "application/json")

    @patch('providers.repository_provider.fetch_order_pool')
    def test_get_order_by_id_not_found(self, mock_repo):
        # Setup
        mock_repo.return_value.get_order.return_value = None
        
        # Execute
        self.controller.get_by_id(self.handler, 999)
        
        # Assert
        self.assertEqual(self.handler.response_code, 404)

    @patch('providers.repository_provider.fetch_order_pool')
    def test_get_items_in_order(self, mock_repo):
        # Setup
        mock_items = [Item(id=1, name="Test Item", quantity=1)]
        mock_repo.return_value.get_items_in_order.return_value = mock_items
        
        # Execute
        self.controller.get_items_in_order(self.handler, 1)
        
        # Assert
        self.assertEqual(self.handler.response_code, 200)
        self.assertEqual(self.handler.headers.get("Content-Type"), "application/json")

    @patch('providers.repository_provider.fetch_order_pool')
    def test_add_order(self, mock_repo):
        # Setup
        self.handler.headers = {"Content-Length": len(json.dumps(self.sample_order.__dict__))}
        self.handler.rfile = MagicMock()
        self.handler.rfile.read.return_value = json.dumps(self.sample_order.__dict__).encode()
        
        # Execute
        self.controller.add_order(self.handler)
        
        # Assert
        self.assertEqual(self.handler.response_code, 201)
        mock_repo.return_value.add_order.assert_called_once()
        mock_repo.return_value.save.assert_called_once()

    @patch('providers.repository_provider.fetch_order_pool')
    def test_update_order(self, mock_repo):
        # Setup
        self.handler.headers = {"Content-Length": len(json.dumps(self.sample_order.__dict__))}
        self.handler.rfile = MagicMock()
        self.handler.rfile.read.return_value = json.dumps(self.sample_order.__dict__).encode()
        
        # Execute
        self.controller.update_order(self.handler, 1)
        
        # Assert
        self.assertEqual(self.handler.response_code, 204)
        mock_repo.return_value.update_order.assert_called_once()
        mock_repo.return_value.save.assert_called_once()

    @patch('providers.repository_provider.fetch_order_pool')
    def test_update_items_in_order(self, mock_repo):
        # Setup
        test_items = [{"id": 1, "name": "Test Item", "quantity": 1}]
        self.handler.headers = {"Content-Length": len(json.dumps(test_items))}
        self.handler.rfile = MagicMock()
        self.handler.rfile.read.return_value = json.dumps(test_items).encode()
        
        # Execute
        self.controller.update_items_in_order(self.handler, 1)
        
        # Assert
        self.assertEqual(self.handler.response_code, 204)
        mock_repo.return_value.update_items_in_order.assert_called_once()
        mock_repo.return_value.save.assert_called_once()

    @patch('providers.repository_provider.fetch_order_pool')
    def test_delete_order(self, mock_repo):
        # Execute
        self.controller.delete_order(self.handler, 1)
        
        # Assert
        self.assertEqual(self.handler.response_code, 204)
        mock_repo.return_value.remove_order.assert_called_once_with(1)
        mock_repo.return_value.save.assert_called_once()

if __name__ == '__main__':
    unittest.main()