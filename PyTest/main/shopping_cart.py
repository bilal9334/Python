class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"


class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not in cart!")

    def total_price(self):
        return sum(product.price for product in self.products)

    def is_empty(self):
        return len(self.products) == 0
