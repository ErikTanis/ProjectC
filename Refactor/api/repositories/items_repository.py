class ItemsRepository(BaseRepository):
    def __init__(self):
        super().__init__("items.json", False)
        self.load()

    def get_items(self):
        return self.items

    def get(self, item_id):
        for x in self.data:
            if x.uid == item_id:
                return x
        return None

    def add(self, item):
        item.created_at = self.get_timestamp()
        item.updated_at = self.get_timestamp()
        self.data.append(item)
        self.save()
        
    def update(self, item_id, item):
        item.updated_at = self.get_timestamp()
        for i in range(len(self.items)):
            if self.items[i].uid == item_id:
                self.items[i] = item
                break
        self.save(self.items)
        
    def remove(self, item_id):
        for x in self.items:
            if x.uid == item_id:
                self.items.remove(x)
        self.save(self.items)

    def load(self):
        data = super().load()
        self.items = [];
        for x in data:
            self.items.append(Item(**x))

    def save(self):
        data = []
        for x in self.items:
            data.append(x.__dict__)
        super().save(data)
