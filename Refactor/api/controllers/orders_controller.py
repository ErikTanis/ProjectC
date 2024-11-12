from providers import repository_provider
import json
import http.server
from models.orders import Order
from models.items import Item

class OrdersController:
    def __init__(self) -> None:
        self.repository = repository_provider.fetch_order_pool()

    def handle_get_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                self.get_by_id(handler, path[1])
            case 3:
                self.get_items_in_order(handler, path[1])
            case _:
                handler.send_response(404)
                handler.end_headers()
    
    def handle_post_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 1:
                self.add_order(handler)
            case _:
                handler.send_response(404)
                handler.end_headers()
    
    def handle_put_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 2:
                self.update_order(handler, path[1])
            case 3:
                if path[2] == "items":
                    self.update_items_in_order(handler, path[1])
                else:
                    handler.send_response(404)
                    handler.end_headers()
            case _:
                handler.send_response(404)
                handler.end_headers()

    def handle_delete_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 2:
                self.delete_order(handler, path[1])
            case _:
                handler.send_response(404)
                handler.end_headers()
    
    # GET /api/v1/orders
    def get_all(self, handler: http.server.BaseHTTPRequestHandler):
        orders = self.repository.get_orders()
        handler.send_response(200)
        handler.send_header("Content-Type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps([order.__dict__ for order in orders]).encode())

    # GET /api/v1/orders/{order_id}
    def get_by_id(self, handler: http.server.BaseHTTPRequestHandler, order_id):
        order = self.repository.get_order(order_id)
        if order:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps(order.__dict__).encode())
        else:
            handler.send_response(404)
            handler.end_headers()
    
    # GET /api/v1/orders/{order_id}/items
    def get_items_in_order(self, handler: http.server.BaseHTTPRequestHandler, order_id):
        items = self.repository.get_items_in_order(order_id)
        if items:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps([item.__dict__ for item in items]).encode())
        else:
            handler.send_response(404)
            handler.end_headers()
    
    # POST /api/v1/orders
    def add_order(self, handler: http.server.BaseHTTPRequestHandler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        order = Order.from_dict(json.loads(post_data))
        self.repository.add_order(order)
        self.repository.save()
        handler.send_response(201)
        handler.end_headers()
        handler.wfile.write(json.dumps(order.__dict__).encode())
    
    # PUT /api/v1/orders/{order_id}
    def update_order(self, handler: http.server.BaseHTTPRequestHandler, order_id):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        order = Order.from_dict(json.loads(post_data))
        self.repository.update_order(order_id, order)
        self.repository.save()
        handler.send_response(204)
        handler.end_headers()
    
    # PUT /api/v1/orders/{order_id}/items
    def update_items_in_order(self, handler: http.server.BaseHTTPRequestHandler, order_id):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        items = [Item.from_dict(item) for item in json.loads(post_data)]
        self.repository.update_items_in_order(order_id, items)
        self.repository.save()
        handler.send_response(204)
        handler.end_headers()
    
    # DELETE /api/v1/orders/{order_id}
    def delete_order(self, handler: http.server.BaseHTTPRequestHandler, order_id):
        self.repository.remove_order(order_id)
        self.repository.save()
        handler.send_response(204)
        handler.end_headers()
