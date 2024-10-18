class Product:
    slots = []
    
    def __init__(self, quantity: int):
        self.__quantity: int = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
