from api.providers import repository_provider
import http.server
import json
from models.shipments import Shipment


class ShipmentsController:
    def __init__(self) -> None:
        self.repository = repository_provider.fetch_shipment_pool()

    def handle_get_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                self.get_by_id(handler, path[1])
            case 3:
                if path[2] == "orders":
                    self.get_orders_in_shipment(handler, path[1])
                if path[2] == "items":
                    self.get_items_in_shipment(handler, path[1])
                else:
                    handler.send_response(404)
                    handler.end_headers()
            case _:
                handler.send_response(404)
                handler.end_headers()

    def handle_post_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 1:
                self.add_shipment(handler)
            case _:
                handler.send_response(404)
                handler.end_headers()

    def handle_put_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 2:
                self.update_shipment(handler, path[1])
            case 3:
                if path[2] == "orders":
                    self.update_orders_in_shipment(handler, path[1])
                if path[2] == "items":
                    self.update_items_in_shipment(handler, path[1])
                if path[2] == "commit":
                    self.commit_shipment(handler, path[1])
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
                self.delete_shipment(handler, path[1])
            case _:
                handler.send_response(404)
                handler.end_headers()

    # GET /api/v1/shipments
    def get_all(self, handler: http.server.BaseHTTPRequestHandler):
        shipments = self.repository.get_shipments()
        handler.send_response(200)
        handler.send_header("Content-Type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps([shipment.__dict__ for shipment in shipments]).encode())

    # GET /api/v1/shipments/{shipment_id}
    def get_by_id(self, handler: http.server.BaseHTTPRequestHandler, shipment_id):
        shipment = self.repository.get_shipment(shipment_id)
        if shipment:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps(shipment.__dict__).encode())
        else:
            handler.send_response(404)
            handler.end_headers()
    
    # GET /api/v1/shipments/{/orders
    def get_orders_in_shipment(self, handler: http.server.BaseHTTPRequestHandler, shipment_id):
        orders = repository_provider.fetch_order_pool().get_orders_in_shipment(shipment_id)
        if orders:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps(orders).encode())
        else:
            handler.send_response(404)
            handler.end_headers()

    # GET /api/v1/shipments/{shipment_id}/items
    def get_items_in_shipment(self, handler: http.server.BaseHTTPRequestHandler, shipment_id):
        items = self.repository.get_items_in_shipment(shipment_id)
        if items:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps(items).encode())
        else:
            handler.send_response(404)
            handler.end_headers()
    
    # POST /api/v1/shipments
    def add_shipment(self, handler: http.server.BaseHTTPRequestHandler):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        shipment = Shipment.from_dict(json.loads(post_data))
        self.repository.add_shipment(shipment)
        self.repository.save()
        handler.send_response(201)
        handler.end_headers()
        handler.wfile.write(json.dumps(shipment.__dict__).encode())
    
    # PUT /api/v1/shipments/{shipment_id}
    def update_shipment(self, handler: http.server.BaseHTTPRequestHandler, shipment_id):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        shipment = Shipment.from_dict(json.loads(post_data))
        self.repository.update_shipment(shipment_id, shipment)
        self.repository.save()
        handler.send_response(204)
        handler.end_headers()

    # PUT /api/v1/shipments/{shipment_id}/orders
    def update_orders_in_shipment(self, handler: http.server.BaseHTTPRequestHandler, shipment_id):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        orders = json.loads(post_data)
        repository_provider.fetch_order_pool().update_orders_in_shipment(shipment_id, orders)
        repository_provider.fetch_order_pool().save()
        handler.send_response(204)
        handler.end_headers()

    # PUT /api/v1/shipments/{shipment_id}/items
    def update_items_in_shipment(self, handler: http.server.BaseHTTPRequestHandler, shipment_id):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        items = json.loads(post_data)
        self.repository.update_items_in_shipment(shipment_id, items)
        self.repository.save()
        handler.send_response(204)
        handler.end_headers()
    
    # PUT /api/v1/shipments/{shipment_id}/commit
    def commit_shipment(self, handler: http.server.BaseHTTPRequestHandler, shipment_id):
        pass

    # DELETE /api/v1/shipments/{shipment_id}
    def delete_shipment(self, handler: http.server.BaseHTTPRequestHandler, shipment_id):
        self.repository.delete_shipment(shipment_id)
        self.repository.save()
        handler.send_response(204)
        handler.end_headers()