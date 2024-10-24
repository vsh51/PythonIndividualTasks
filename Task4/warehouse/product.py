class Product():
    __slots__ = ['name', 'price', 'quantity']

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def __iadd__(self, amount: int):
        self.quantity += amount
        return self

    def __isub__(self, amount: int):
        self.quantity -= amount
        return self
