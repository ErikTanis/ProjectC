# from api.repositories.warehouses_repository import WarehousesRepository
# from api.repositories.locations_repository import LocationsRepository
# from api.repositories.transfers_repository import TransfersRepository
from api.repositories.items_repository import ItemsRepository
from api.repositories.item_lines_repository import ItemLinesRepository
from api.repositories.item_groups_repository import ItemGroupsRepository
from api.repositories.item_types_repository import ItemTypesRepository
from api.repositories.inventories_repository import InventoriesRepository
# from api.repositories.suppliers_repository import SuppliersRepository
# from api.repositories.orders_repository import OrdersRepository
# from api.repositories.clients_repository import ClientsRepository
# from api.repositories.shipments_repository import ShipmentsRepository

DEBUG = True
ROOT_PATH = "data/"
_warehouses = None
_locations = None
_transfers = None
_items = None
_item_lines = None
_item_groups = None
_item_types = None
_inventories = None
_suppliers = None
_orders = None
_shipments = None
_clients = None

def init():
    # global _warehouses
    # _warehouses = WarehousesRepository(ROOT_PATH, DEBUG)
    # global _locations
    # _locations = LocationsRepository(ROOT_PATH, DEBUG)
    # global _transfers
    # _transfers = TransfersRepository(ROOT_PATH, DEBUG)
    global _items
    _items = ItemsRepository(ROOT_PATH, DEBUG)
    global _item_lines
    _item_lines = ItemLinesRepository(ROOT_PATH, DEBUG)
    global _item_groups
    _item_groups = ItemGroupsRepository(ROOT_PATH, DEBUG)
    global _item_types
    _item_types = ItemTypesRepository(ROOT_PATH, DEBUG)
    global _inventories
    _inventories = InventoriesRepository(ROOT_PATH, DEBUG)
    # global _suppliers
    # _suppliers = SuppliersRepository(ROOT_PATH, DEBUG)
    # global _orders
    # _orders = OrdersRepository(ROOT_PATH, DEBUG)
    # global _clients
    # _clients = ClientsRepository(ROOT_PATH, DEBUG)
    # global _shipments
    # _shipments = ShipmentsRepository(ROOT_PATH, DEBUG)

def fetch_warehouse_pool():
    return _warehouses

def fetch_location_pool():
    return _locations

def fetch_transfer_pool():
    return _transfers

def fetch_item_pool():
    return _items

def fetch_item_line_pool():
    return _item_lines

def fetch_item_group_pool():
    return _item_groups

def fetch_item_type_pool():
    return _item_types

def fetch_inventory_pool():
    return _inventories

def fetch_supplier_pool():
    return _suppliers

def fetch_order_pool():
    return _orders

def fetch_client_pool():
    return _clients

def fetch_shipment_pool():
    return _shipments
