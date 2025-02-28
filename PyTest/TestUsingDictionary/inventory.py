class Product:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Quantity: {self.quantity}"


class Inventory:

    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, quantity)

    def remove_product(self, name, quantity):
        if name not in self.products:
            raise KeyError("Product not found.")

        if quantity >= self.products[name].quantity:
            del self.products[name]
        else:
            self.products[name].quantity -= quantity

    def get_product_quantity(self, name):
        if name not in self.products:
            raise KeyError("Product not found.")
        return self.products[name].quantity

    def get_all_products(self):
        return {name: product.quantity for name, product in self.products.items()}
