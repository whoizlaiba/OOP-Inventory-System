import json
from item import Tech, Food, Wear

class InventoryManager:
    def __init__(self):
        self._items = {}

    def add(self, item):
        if item.get_id() in self._items:
            raise KeyError("Duplicate ID.")
        self._items[item.get_id()] = item

    def delete(self, id):
        if id in self._items:
            del self._items[id]

    def sell(self, id, qty):
        if id in self._items:
            self._items[id].sell(qty)

    def restock(self, id, qty):
        if id in self._items:
            self._items[id].add_stock(qty)

    def search_name(self, keyword):
        return [x for x in self._items.values() if keyword.lower() in x.get_title().lower()]

    def search_type(self, typename):
        return [x for x in self._items.values() if x.get_type().lower() == typename.lower()]

    def display(self):
        return [x.info() for x in self._items.values()]

    def total_value(self):
        return sum(x.value() for x in self._items.values())

    def clear_expired(self):
        remove_ids = [id for id, item in self._items.items() if isinstance(item, Food) and item.expired()]
        for id in remove_ids:
            del self._items[id]

    def save(self, path):
        data = []
        for x in self._items.values():
            d = {
                "type": x.get_type(),
                "id": x.get_id(),
                "title": x.get_title(),
                "price": x._price,
                "stock": x._stock
            }
            if isinstance(x, Tech):
                d["brand"] = x.brand
                d["warranty"] = x.warranty
            elif isinstance(x, Food):
                d["expiry"] = x.expiry.strftime("%Y-%m-%d")
            elif isinstance(x, Wear):
                d["size"] = x.size
                d["fabric"] = x.fabric
            data.append(d)
        with open(path, "w") as f:
            json.dump(data, f)

    def load(self, path):
        with open(path, "r") as f:
            loaded = json.load(f)
        for obj in loaded:
            t = obj["type"]
            if t == "Tech":
                item = Tech(obj["id"], obj["title"], obj["price"], obj["stock"], obj["brand"], obj["warranty"])
            elif t == "Food":
                item = Food(obj["id"], obj["title"], obj["price"], obj["stock"], obj["expiry"])
            elif t == "Wear":
                item = Wear(obj["id"], obj["title"], obj["price"], obj["stock"], obj["size"], obj["fabric"])
            else:
                continue
            self._items[item.get_id()] = item
