class Item:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __str__(self):
        return f"Item: {self.item}, Price: {self.price}"


class ShoppingCart:

    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = Item(item, price)

    def remove_item(self, item):
        if item not in self.items:
            raise ValueError("Item not found!")
        del self.items[item]

    def get_total(self):
        return sum(item.price for item in self.items.values())

    def get_items(self):
        return {item: obj.price for item, obj in self.items.items()}
