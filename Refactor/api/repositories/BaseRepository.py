import json
import sys
import os

class BaseRepository:
    def __init__(self, path, is_debug):
        self.path = os.path.join(sys.path[0], "data", path)
        self.is_debug = is_debug

    def save(self, data: list[dict]):
        if self.is_debug:
            return
        
        with open(self.path, 'w', encoding='utf8', newline='') as file:
            json.dump(data, file, indent=4)

    def load(self) -> list[dict]:
        if self.is_debug:
            return []
        
        if not os.path.exists(self.path):
            return list()
        with open(self.path, encoding='utf8') as file:
            return json.load(file)