import json
import os
import sys
from datetime import datetime
from json.decoder import JSONDecodeError

class BaseRepository:
    def __init__(self, file_name: str, path: str = None, is_debug: bool = False):
        if(path == None):
            path = sys.path[0]

        self.path = os.path.abspath(os.path.join(path, file_name))
        self.is_debug = is_debug
        
    def save(self, data: list[dict]) -> bool:
        if self.is_debug:
            print(f"[DEBUG] Would save data to {self.path}")
            return True

        try:
            with open(self.path, 'w', encoding='utf8', newline='') as file:
                json.dump(data, file, indent=4)
            return True
        except IOError as e:
            print(f"Error saving data to {self.path}: {e}")
            return False

    def load(self) -> list[dict]:
        if self.is_debug:
            print(f"[DEBUG] Would load data from {self.path}")
            return []
        
        if not os.path.exists(self.path):
            return list()
        
        try:
            with open(self.path, encoding='utf8') as file:
                return json.load(file)
        except (IOError, JSONDecodeError) as e:
            print(f"Error loading data from {self.path}: {e.__class__.__name__} - {e}")
            return []

    def get_timestamp(self) -> str:
        return datetime.utcnow().isoformat() + "Z"
