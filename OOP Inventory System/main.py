from manager import InventoryManager
from item import Tech, Food, Wear

inv = InventoryManager()

while True:
    print("\n1.Add 2.Sell 3.Restock 4.Search Name 5.Search Type 6.View All 7.Total Value 8.Remove Expired 9.Save 10.Load 11.Exit")
    choice = input("Select: ")
    if choice == "1":
        kind = input("Type (Tech/Food/Wear): ")
        id = input("ID: ")
        name = input("Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        if kind.lower() == "tech":
            brand = input("Brand: ")
            warranty = int(input("Warranty (years): "))
            p = Tech(id, name, price, stock, brand, warranty)
        elif kind.lower() == "food":
            expiry = input("Expiry (YYYY-MM-DD): ")
            p = Food(id, name, price, stock, expiry)
        elif kind.lower() == "wear":
            size = input("Size: ")
            fabric = input("Fabric: ")
            p = Wear(id, name, price, stock, size, fabric)
        else:
            continue
        try:
            inv.add(p)
        except:
            print("ID already exists.")
    elif choice == "2":
        id = input("ID: ")
        q = int(input("Qty: "))
        try:
            inv.sell(id, q)
        except:
            print("Error in selling.")
    elif choice == "3":
        id = input("ID: ")
        q = int(input("Qty: "))
        inv.restock(id, q)
    elif choice == "4":
        keyword = input("Search: ")
        for p in inv.search_name(keyword):
            print(p.info())
    elif choice == "5":
        t = input("Type: ")
        for p in inv.search_type(t):
            print(p.info())
    elif choice == "6":
        for p in inv.display():
            print(p)
    elif choice == "7":
        print("Total Rs.", inv.total_value())
    elif choice == "8":
        inv.clear_expired()
    elif choice == "9":
        path = input("Filename: ")
        inv.save(path)
    elif choice == "10":
        path = input("Filename: ")
        inv.load(path)
    elif choice == "11":
        break
