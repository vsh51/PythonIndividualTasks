from warehouse.product import Product
import time


class ProductManager:
    def __init__(self, is_admin: bool = False):
        self.is_admin = is_admin

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.is_admin:
                return func(*args, **kwargs)
            raise Exception("You are not admin")
        return wrapper


class Warehouse:
    @staticmethod
    def log_time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            print(f"[{start}] Started executing {func.__name__}")
            result = func(*args, **kwargs)
            end = time.time()
            print(f"[{end}] Finished executing {func.__name__}")
            return result
        return wrapper

    @staticmethod
    def price_filter(warehouse, min_price:float, max_price:float):
        fittable_products:list[str] = []
        for product in warehouse.products.values():
            if min_price <= product.price <= max_price:
                fittable_products.append(product)
        return fittable_products

    def __init__(self):
        self.products:dict[str, Product] = {}

    @ProductManager(is_admin=True)
    @log_time
    def add_product(self, product:Product):
        self.products[product.name] = product

    @ProductManager(is_admin=True)
    @log_time
    def get_product(self, name:str) -> Product:
        return self.products[name]

    @log_time
    def dump(self, filename:str):
        with open (filename, 'w') as file:
            for product in self.products.values():
                file.write(f"{str(product)}\n")


class WarehouseManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.warehouse = Warehouse()

    def __enter__(self):
        open(self.filename, 'a').close()
        self.warehouse = Warehouse()
        return self.warehouse

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.warehouse.dump(self.filename)
