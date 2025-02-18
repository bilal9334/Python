class ShoppingCart:
    """Simple class to add, remove, and view the items in a cart

    Args:
        __items [List]: A list of all items in the cart.

    Methods:
        add_item: This adds items to the shopping cart.
        remove_item: Remove the item if it already exists in the cart.
        view_cart: All items in the cart can be viewed.
    """

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        print(f"{item} added to the cart")

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print(f"{item} removed from the cart")
        else:
            print(f"{item} is not in the cart")

    def view_cart(self):
        """Display the items in the cart"""
        if self.__items:
            print(f"Cart contains: {self.__items}")
        else:
            print("Cart is empty")

    def clear_cart(self):
        """Empties the cart"""
        self.__items.clear()
        print("Cart has been emptied!")


if __name__ == '__main__':
    cart = ShoppingCart()

    cart.add_item("Laptop")
    cart.add_item("Headphones")
    cart.view_cart()

    cart.remove_item("Laptop")
    cart.view_cart()

    # Trying to access the private attribute (should fail)
    try:
        print(cart.__items)  # This should rais an AttributeError
    except AttributeError:
        print("Direct access to items is not allowed!")

    cart.clear_cart()
    cart.view_cart()
