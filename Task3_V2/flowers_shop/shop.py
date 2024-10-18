from .flower import Flower, FlowerBuilder
import csv

class Shop:
    @staticmethod
    def calculate_total_price(products: list[Flower]):
        return sum([product.total_price() for product in products])

    def __init__(self):
        self.products: list[Flower] = []

    def add_product(self, product: Flower):
        self.products.append(product)

    def read_products(self, filepath: str):
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            store_data = list(reader)
            store_data.pop(0)
            
            for data in store_data:
                processed_data = [data[0], data[1], int(data[2]), float(data[3])]
                processed_data.extend(data[4:])

                flower = FlowerBuilder.build(processed_data)
                self.add_product(flower)

    def get_products(self):
        return self.products

    def __str__(self):
        return '\n'.join([str(product) for product in self.products])
