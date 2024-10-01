import json
class LocationsRepository(BaseRepository):
    def __init__(self):
        super().__init__("locations.json", False)
        self.load()

    def get_locations(self):
        return self.locations

    def get(self, location_id):
        for x in self.locations:
            if x["id"] == location_id:
                return x
        return None

    def get_locations_in_warehouse(self, warehouse_id):
        result = []
        for x in self.locations:
            if x["warehouse_id"] == warehouse_id:
                result.append(x)
        return result

    def add(self, location):
        location["created_at"] = self.get_timestamp()
        location["updated_at"] = self.get_timestamp()
        self.locations.append(location)
        self.save()

    def update(self, location_id, location):
        location["updated_at"] = self.get_timestamp()
        for i in range(len(self.locations)):
            if self.locations[i]["id"] == location_id:
                self.locations[i] = location
                break
        self.save()

    def remove(self, location_id):
        for x in self.locations:
            if x["id"] == location_id:
                self.locations.remove(x)
        self.save()

    def load(self):
        data = super().load()
        self.locations = []
        for x in data:
            self.locations.append(Location(**x))

    def save(self):
        data = []
        for x in self.locations:
            data.append(x.__dict__)
        super().save(data)