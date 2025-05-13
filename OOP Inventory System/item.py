from abc import ABC, abstractmethod
from datetime import datetime

class Item(ABC):
    def __init__(self, id, title, price, stock):
        self._id = id
        self._title = title
        self._price = price
        self._stock = stock

    @abstractmethod
    def info(self):
        pass

    def add_stock(self, count):
        self._stock += count

    def sell(self, count):
        if count > self._stock:
            raise ValueError("Not enough stock available.")
        self._stock -= count

    def value(self):
        return self._price * self._stock

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_stock(self):
        return self._stock

    def get_type(self):
        return self.__class__.__name__

class Tech(Item):
    def __init__(self, id, title, price, stock, brand, warranty):
        super().__init__(id, title, price, stock)
        self.brand = brand
        self.warranty = warranty

    def info(self):
        return f"{self._title} [{self.brand}, {self.warranty} yrs] - Rs.{self._price} ({self._stock} in stock)"

class Food(Item):
    def __init__(self, id, title, price, stock, expiry):
        super().__init__(id, title, price, stock)
        self.expiry = datetime.strptime(expiry, "%Y-%m-%d")

    def expired(self):
        return datetime.now() > self.expiry

    def info(self):
        status = "Expired" if self.expired() else "Fresh"
        return f"{self._title} [{status}] - Rs.{self._price} ({self._stock} in stock)"

class Wear(Item):
    def __init__(self, id, title, price, stock, size, fabric):
        super().__init__(id, title, price, stock)
        self.size = size
        self.fabric = fabric

    def info(self):
        return f"{self._title} [{self.size}, {self.fabric}] - Rs.{self._price} ({self._stock} in stock)"
