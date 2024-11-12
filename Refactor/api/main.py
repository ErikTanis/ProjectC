from repositories.orders_repository import OrdersRepository
from models.orders import Order

a = OrdersRepository('orders.json')

print(a.get_orders())

test = Order(0, 1, '2022-01-01', '2022-01-01', 'ref', 'ref_extra', 'status', 'notes', 'shipping_notes', 'picking_notes', 1, 'ship_to', 'bill_to', 1, 1, 1, 1, 1, '2022-01-01', '2022-01-01', [])
a.add_order("test")

print()

print(a.get_order(0).to_dict())
