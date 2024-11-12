from api.providers import repository_provider
import http.server
import json
from models.suppliers import Supplier


class SuppliersController:
    def __init__(self) -> None:
        self.repository = repository_provider.fetch_supplier_pool()

    def handle_get_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                self.get_by_id(handler, path[1])
            case 3:
                if path[2] == "items":
                    self.get_items_for_supplier(handler, path[1])
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
                self.add_supplier(handler)
            case _:
                handler.send_response(404)
                handler.end_headers()

    def handle_put_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 2:
                self.update_supplier(handler, path[1])
            case _:
                handler.send_response(404)
                handler.end_headers()

    def handle_delete_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 2:
                self.delete_supplier(handler, path[1])
            case _:
                handler.send_response(404)
                handler.end_headers()
    
    # GET /api/v1/suppliers
    def get_all(self, handler: http.server.BaseHTTPRequestHandler):
        suppliers = self.repository.get_suppliers()
        handler.send_response(200)
        handler.send_header("Content-Type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps([supplier.__dict__ for supplier in suppliers]).encode())

    # GET /api/v1/suppliers/{supplier_id}
    def get_by_id(self, handler: http.server.BaseHTTPRequestHandler, supplier_id):
        supplier = self.repository.get_supplier(supplier_id)
        if supplier:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps(supplier.__dict__).encode())
        else:
            handler.send_response(404)
            handler.end_headers()
    
    # GET /api/v1/suppliers/{supplier_id}/items
    def get_items_for_supplier(self, handler: http.server.BaseHTTPRequestHandler, supplier_id):
        items = repository_provider.fetch_item_pool().get_items_for_supplier(supplier_id)
        if items:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps([item.__dict__ for item in items]).encode())
        else:
            handler.send_response(404)
            handler.end_headers()

    # POST /api/v1/suppliers
    def add_supplier(self, handler: http.server.BaseHTTPRequestHandler):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        supplier = Supplier.from_dict(json.loads(post_data))
        self.repository.add_supplier(supplier)
        handler.send_response(201)
        handler.send_header("Content-Type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(supplier.__dict__).encode())

    # PUT /api/v1/suppliers/{supplier_id}
    def update_supplier(self, handler: http.server.BaseHTTPRequestHandler, supplier_id):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        supplier = Supplier.from_dict(json.loads(post_data))
        self.repository.update_supplier(supplier_id, supplier)
        handler.send_response(200)
        handler.send_header("Content-Type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(supplier.__dict__).encode())


    # DELETE /api/v1/suppliers/{supplier_id}
    def delete_supplier(self, handler: http.server.BaseHTTPRequestHandler, supplier_id):
        self.repository.remove_supplier(supplier_id)
        handler.send_response(204)
        handler.end_headers()

