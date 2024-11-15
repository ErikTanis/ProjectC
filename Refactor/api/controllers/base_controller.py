import json

class BaseController:
    def respond_ok(self, handler, data = None):
        handler.send_response(200)
        if data:
            handler.send_header("Content-type", "application/json")
            handler.end_headers()
            handler.wfile.write(
                json.dumps([entry.__dict__ for entry in data]).encode("utf-8")
            )
        else:
            handler.end_headers()

    def respond_not_found(self, handler):
        handler.send_response(404)
        handler.end_headers()

    def respond_created(self, handler, data):
        handler.send_response(201)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(
            json.dumps([entry.__dict__ for entry in data]).encode("utf-8")
        )

    def respond_no_content(self, handler):
        handler.send_response(204)
        handler.end_headers()

    def get_json_body(self, handler):
        content_length = int(handler.headers["Content-Length"])
        data = handler.rfile.read(content_length)
        return json.loads(data.decode())