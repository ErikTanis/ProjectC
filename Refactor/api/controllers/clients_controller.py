from api.providers import repository_provider
import http.server
import json
from models.clients import Client


class ClientsController:
    def __init__(self) -> None:
        self.repository = repository_provider.fetch_client_pool()

    def handle_get_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                self.get_by_id(handler, path[1])
            case 3:
                if path[2] == "orders":
                    self.get_orders_for_client(handler, path[1])
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
                self.add_client(handler)
            case _:
                handler.send_response(404)
                handler.end_headers()

    def handle_put_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 2:
                self.update_client(handler, path[1])
            case _:
                handler.send_response(404)
                handler.end_headers()

    def handle_delete_version_1(self, path, handler: http.server.BaseHTTPRequestHandler):
        paths = len(path)
        match paths:
            case 2:
                self.delete_client(handler, path[1])
            case _:
                handler.send_response(404)
                handler.end_headers()

    # GET /api/v1/clients
    def get_all(self, handler: http.server.BaseHTTPRequestHandler):
        clients = self.repository.get_clients()
        handler.send_response(200)
        handler.send_header("Content-Type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps([client.__dict__ for client in clients]).encode())

    # GET /api/v1/clients/{client_id}
    def get_by_id(self, handler: http.server.BaseHTTPRequestHandler, client_id):
        client = self.repository.get_client(client_id)
        if client:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps(client.__dict__).encode())
        else:
            handler.send_response(404)
            handler.end_headers()
    
    # GET /api/v1/clients/{client_id}/orders
    def get_orders_for_client(self, handler: http.server.BaseHTTPRequestHandler, client_id):
        orders = repository_provider.fetch_order_pool().get_orders_for_client(client_id)
        if orders:
            handler.send_response(200)
            handler.send_header("Content-Type", "application/json")
            handler.end_headers()
            handler.wfile.write(json.dumps([order.__dict__ for order in orders]).encode())
        else:
            handler.send_response(404)
            handler.end_headers()

    # POST /api/v1/clients
    def add_client(self, handler: http.server.BaseHTTPRequestHandler):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        client = Client(**json.loads(post_data))
        self.repository.add_client(client)
        handler.send_response(201)
        handler.end_headers()

    # PUT /api/v1/clients/{client_id}
    def update_client(self, handler: http.server.BaseHTTPRequestHandler, client_id):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length)
        client = Client(**json.loads(post_data))
        self.repository.update_client(client_id, client)
        handler.send_response(204)
        handler.end_headers()

    # DELETE /api/v1/clients/{client_id}
    def delete_client(self, handler: http.server.BaseHTTPRequestHandler, client_id):
        self.repository.delete_client(client_id)
        handler.send_response(204)
        handler.end_headers()