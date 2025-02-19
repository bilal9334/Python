class Product:
    """Managing prices of the product for customers"""

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        if amount >= 0:
            self.__price = amount
        else:
            print("Amount cannot be negative!")

    @property
    def discount_price(self):
        return self.__price * 0.9


if __name__ == '__main__':
    item = Product("Laptop", 1000)
    print(item.price)

    print(item.discount_price)

    item.price = -500
