from api.providers import repository_provider
from Base_controller import BaseController
from api.models.locations import Location

class LocationsController(BaseController):
    def __init__(self):
        self.provider = repository_provider

    def handle_get_version_1(self, path, handler):
        paths = len(path)
        match paths:
            case 1:
                self.get_all(handler)
            case 2:
                location_id = int(path[1])
                self.get_by_id(handler, location_id)
            case _:
                self.respond_not_found(handler)

    def handle_post_version_1(self, handler):
        self.add(handler)

    def handle_put_version_1(self, path, handler):
        location_id = int(path[1])
        self.update(handler, location_id)

    def handle_delete_version_1(self, path, handler):
        location_id = int(path[1])
        self.delete(handler, location_id)

    # /api/v1/locations
    def get_all(self, handler):
        locations = self.provider.fetch_location_pool().get_all()
        self.respond_ok(handler, locations)

    # /api/v1/locations/{location_id}
    def get_by_id(self, handler, location_id):
        location = self.provider.fetch_location_pool().get_by_id(location_id)
        self.respond_ok(handler, location)

    # /api/v1/locations
    def add(self, handler):
        content = self.get_json_body(handler)
        location = Location.from_dict(content)
        self.provider.fetch_location_pool().add(location)
        self.respond_ok(handler, location)

    # /api/v1/locations/{location_id}
    def update(self, handler, location_id):
        content = self.get_json_body(handler)
        location = Location.from_dict(content)
        self.provider.fetch_location_pool().update(location_id, location)
        self.respond_ok(handler, location)

    # /api/v1/locations/{location_id}
    def delete(self, handler, location_id):
        self.provider.fetch_location_pool().remove(location_id)
        self.respond_ok(handler, None)