from .product import Product

class FlowerBuilder:
    @staticmethod
    def build(data: list):
        flower: Flower

        if data[0] == 'Rose':
            flower = Rose(data[1], data[2], data[3], data[4])
        elif data[0] == 'Tulip':
            flower = Tulip(data[1], data[2], data[3], data[4])
        elif data[0] == 'Lily':
            flower = Lily(data[1], data[2], data[3], data[4])
        else:
            flower = Flower(data[0], data[1], data[2], data[3])

        return flower


class Flower(Product):
    __slots__ = ['_name', '_color', '_quantity', '_price']

    def __init__(self, name, color, quantity:int, price: float):
        Product.__init__(self, quantity)
        self._name = name
        self._color = color
        self._price = price

    def __str__(self):
        return f'{self.name} | {self.color} | {self.quantity} | {self.price}'

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def price(self):
        return self._price

    @name.setter
    def name(self, name):
        self._name = name

    @color.setter
    def color(self, color):
        self._color = color

    @price.setter
    def price(self, price):
        self._price = price

    def total_price(self):
        return self.price * self.quantity


class Rose(Flower):
    __slots__ = ['_length']

    def __init__(self, color, quantity: int, price: float, length):
        Flower.__init__(self, 'Rose', color, quantity, price)
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    def __str__(self):
        
        return Flower.__str__(self) + f' | {self.length}'

class Tulip(Flower):
    __slots__ = ['_kind']

    def __init__(self, color, quantity: int, price: float, kind):
        Flower.__init__(self, 'Tulip', color, quantity, price)
        self._kind = kind

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = kind

    def __str__(self):
        return Flower.__str__(self) + f' | {self.kind}'


class Lily(Flower):
    __slots__ = ['_fragrance']

    def __init__(self, color, quantity: int, price: float, fragrance):
        Flower.__init__(self, 'Lily', color, quantity, price)
        self._fragrance = fragrance

    @property
    def fragrance(self):
        return self._fragrance

    @fragrance.setter
    def fragrance(self, fragrance):
        self._fragrance = fragrance

    def __str__(self):
        return Flower.__str__(self) + f' | {self.fragrance}'
