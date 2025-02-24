class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Order:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)

    def apply_discount(self, percentage):
        if not self.products:
            return 0

        total_price = self.total_price()

        return total_price * (1 - percentage / 100)

    def is_empty(self):
        return len(self.products) == 0

    def checkout(self):
        if not self.products:
            raise ValueError("Order is empty! Failed to checkout")
        else:
            return "Checkout Successful!"
