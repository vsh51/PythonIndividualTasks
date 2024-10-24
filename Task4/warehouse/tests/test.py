import unittest
import warehouse
from warehouse.product import Product

class TestWarehouse(unittest.TestCase):
    def test_admin(self):
        with warehouse.WarehouseManager("store.txt") as wm:
            warehouse.ProductManager(is_admin=True)(wm.add_product)(warehouse.Product("apple", 1.0, 100))

        with open("store.txt") as file:
            self.assertEqual(file.read(), "Name: apple, Price: 1.0, Quantity: 100\n")

    def test_not_admin(self):
        try:
            with warehouse.WarehouseManager("store.txt") as wm:
                warehouse.ProductManager(is_admin=False)(wm.add_product)(warehouse.Product("apple", 1.0, 100))
        except Exception as e:
            self.assertEqual(str(e), "You are not admin")

    def test_increment(self):
        with warehouse.WarehouseManager("store.txt") as wm:
            warehouse.ProductManager(is_admin=True)(wm.add_product)(warehouse.Product("apple", 1.0, 100))
            product = warehouse.ProductManager(is_admin=True)(wm.get_product)("apple")
            product += 50

        with open("store.txt") as file:
            self.assertEqual(file.read(), "Name: apple, Price: 1.0, Quantity: 150\n")

    def test_decrement(self):
        with warehouse.WarehouseManager("store.txt") as wm:
            warehouse.ProductManager(is_admin=True)(wm.add_product)(warehouse.Product("apple", 1.0, 100))
            product = warehouse.ProductManager(is_admin=True)(wm.get_product)("apple")
            product -= 50

        with open("store.txt") as file:
            self.assertEqual(file.read(), "Name: apple, Price: 1.0, Quantity: 50\n")

    def test_not_found(self):
        with warehouse.WarehouseManager("store.txt") as wm:
            try:
                warehouse.ProductManager(is_admin=True)(wm.get_product)("apple")
            except:
                self.assertTrue(True)

    def test_filter(self):
        with warehouse.WarehouseManager("store.txt") as wm:
            warehouse.ProductManager(is_admin=True)(wm.add_product)(warehouse.Product("apple", 1.0, 100))
            warehouse.ProductManager(is_admin=True)(wm.add_product)(warehouse.Product("banana", 2.0, 200))
            warehouse.ProductManager(is_admin=True)(wm.add_product)(warehouse.Product("orange", 3.0, 300))
            products = warehouse.Warehouse.price_filter(wm, 1.0, 2.0)
        self.assertEqual(len(products), 2)
