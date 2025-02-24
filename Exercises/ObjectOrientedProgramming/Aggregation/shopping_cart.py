class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product - {self.name} is {self.price}$"


class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        if not self.products:
            return "Shopping cart is empty"

        total_price = 0
        for product in self.products:
            total_price += product.price  # Sum of product prices

        return f"Total Price: {total_price}"

    def show_cart(self):
        if not self.products:
            return "Shopping cart is empty"

        cart_details = "\n".join(str(product) for product in self.products)
        return f"Shopping Cart: \n{cart_details}\n{self.total_price()}"


if __name__ == '__main__':
    product1 = Product("Laptop", 1000)
    product2 = Product("Mouse", 50)
    product3 = Product("Keyboard", 250)

    cart = ShoppingCart()
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    print(cart.show_cart())
