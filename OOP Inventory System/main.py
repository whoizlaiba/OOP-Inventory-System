# type: ignore
from abc import ABC, abstractmethod
import json
import os

DATA_FILE = "stock_data.json"

class Item(ABC):
    def __init__(self, item_id, title, cost, stock):
        self._item_id = item_id
        self.title = title
        self._cost = cost
        self.stock = stock

    @abstractmethod
    def refill(self, amount):
        pass

    @abstractmethod
    def purchase(self, amount):
        pass

    def get_id(self):
        return self._item_id

    def get_value(self):
        return self._cost * self.stock

    def __str__(self):
        return f"ID: {self._item_id}, Title: {self.title}, Cost: {self._cost}, Stock: {self.stock}"

class Tech(Item):
    def __init__(self, item_id, title, cost, stock, brand, warranty):
        super().__init__(item_id, title, cost, stock)
        self.brand = brand
        self.warranty = warranty

    def refill(self, amount):
        self.stock += amount

    def purchase(self, amount):
        if self.stock >= amount:
            self.stock -= amount
        else:
            print("⚠️ Not enough stock available.")

    def __str__(self):
        return super().__str__() + f", Brand: {self.brand}, Warranty: {self.warranty}"

class Food(Item):
    def __init__(self, item_id, title, cost, stock, expiry):
        super().__init__(item_id, title, cost, stock)
        self.expiry = expiry

    def refill(self, amount):
        self.stock += amount

    def purchase(self, amount):
        if self.stock >= amount:
            self.stock -= amount
        else:
            print("⚠️ Not enough stock available.")

    def is_expired(self):
        return self.expiry < "2025-10-01"

    def __str__(self):
        return super().__str__() + f", Expiry: {self.expiry}"

class Outfit(Item):
    def __init__(self, item_id, title, cost, stock, size, fabric):
        super().__init__(item_id, title, cost, stock)
        self.size = size
        self.fabric = fabric

    def refill(self, amount):
        self.stock += amount

    def purchase(self, amount):
        if self.stock >= amount:
            self.stock -= amount
        else:
            print("⚠️ Not enough stock available.")

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Fabric: {self.fabric}"

class Store:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for i in self.items:
            if i.get_id() == item.get_id():
                print("❌ Duplicate ID found.")
                return
        self.items.append(item)
        print("✅ Item added.")

    def delete_item(self, item_id):
        for i in self.items:
            if i.get_id() == item_id:
                self.items.remove(i)
                print("✅ Item deleted.")
                return
        print("❌ Item not found.")

    def find_by_name(self, name):
        for i in self.items:
            if i.title.lower() == name.lower():
                return i
        return None

    def find_by_type(self, category):
        result = []
        for i in self.items:
            if type(i).__name__.lower() == category.lower():
                result.append(i)
        return result

    def show_all(self):
        if not self.items:
            print("❌ No items to show.")
        for i in self.items:
            print(i)

    def sell_item(self, item_id, qty):
        for i in self.items:
            if i.get_id() == item_id:
                i.purchase(qty)
                print("✅ Item sold.")
                return
        print("❌ Item not found.")

    def refill_item(self, item_id, qty):
        for i in self.items:
            if i.get_id() == item_id:
                i.refill(qty)
                print("✅ Item restocked.")
                return
        print("❌ Item not found.")

    def total_value(self):
        return sum(i.get_value() for i in self.items)

    def clear_expired(self):
        removed = False
        for i in self.items:
            if isinstance(i, Food) and i.is_expired():
                self.items.remove(i)
                print("✅ Expired item removed.")
                removed = True
                break
        if not removed:
            print("❌ No expired items.")

    def save(self):
        data = []
        for i in self.items:
            entry = {
                "type": type(i).__name__,
                "item_id": i.get_id(),
                "title": i.title,
                "cost": i._cost,
                "stock": i.stock
            }
            if isinstance(i, Tech):
                entry.update({"brand": i.brand, "warranty": i.warranty})
            elif isinstance(i, Food):
                entry.update({"expiry": i.expiry})
            elif isinstance(i, Outfit):
                entry.update({"size": i.size, "fabric": i.fabric})
            data.append(entry)
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return
        for d in data:
            if d["type"] == "Tech":
                obj = Tech(d["item_id"], d["title"], d["cost"], d["stock"], d["brand"], d["warranty"])
            elif d["type"] == "Food":
                obj = Food(d["item_id"], d["title"], d["cost"], d["stock"], d["expiry"])
            elif d["type"] == "Outfit":
                obj = Outfit(d["item_id"], d["title"], d["cost"], d["stock"], d["size"], d["fabric"])
            else:
                continue
            self.items.append(obj)

def main():
    store = Store()
    store.load()
    print("📦 Welcome to Easy Inventory System")

    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Delete Item")
        print("3. Search by Name")
        print("4. Search by Category")
        print("5. List All Items")
        print("6. Sell Item")
        print("7. Restock Item")
        print("8. View Total Inventory Value")
        print("9. Remove Expired Items")
        print("10. Exit")
        choice = input("Select option: ")

        if choice == "1":
            id = int(input("ID: "))
            name = input("Title: ")
            cost = float(input("Cost: "))
            qty = int(input("Stock: "))
            category = input("Type (Tech, Food, Outfit): ").lower()
            if category == "tech":
                brand = input("Brand: ")
                warranty = input("Warranty: ")
                item = Tech(id, name, cost, qty, brand, warranty)
            elif category == "food":
                expiry = input("Expiry (YYYY-MM-DD): ")
                item = Food(id, name, cost, qty, expiry)
            elif category == "outfit":
                size = input("Size: ")
                fabric = input("Fabric: ")
                item = Outfit(id, name, cost, qty, size, fabric)
            else:
                print("❌ Invalid type.")
                continue
            store.add_item(item)
            store.save()

        elif choice == "2":
            id = int(input("Enter ID to delete: "))
            store.delete_item(id)
            store.save()

        elif choice == "3":
            name = input("Enter item name: ")
            item = store.find_by_name(name)
            if item:
                print(item)
            else:
                print("❌ Not found.")

        elif choice == "4":
            category = input("Enter type (Tech, Food, Outfit): ")
            result = store.find_by_type(category)
            if result:
                for r in result:
                    print(r)
            else:
                print("❌ No items in this category.")

        elif choice == "5":
            store.show_all()

        elif choice == "6":
            id = int(input("ID to sell: "))
            qty = int(input("Quantity: "))
            store.sell_item(id, qty)
            store.save()

        elif choice == "7":
            id = int(input("ID to restock: "))
            qty = int(input("Quantity: "))
            store.refill_item(id, qty)
            store.save()

        elif choice == "8":
            total = store.total_value()
            print(f"💰 Total Inventory Value: {total}")

        elif choice == "9":
            store.clear_expired()
            store.save()

        elif choice == "10":
            store.save()
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid option.")

if __name__ == "__main__":
    main()
