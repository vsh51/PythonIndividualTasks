import flowers_shop as fstr

def main():
    shop = fstr.Shop()
    shop.read_products('store.csv')
    print(shop)

    shop.add_product(fstr.FlowerBuilder.build(['Orchid', 'White', 10, 5.34]))
    print()

    print(shop)
    print()

    print("Total price:", shop.calculate_total_price(shop.get_products()))

if __name__ == '__main__':
    main()
