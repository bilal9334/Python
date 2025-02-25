class Item:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}"


class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError(f"{item.name} not found in inventory!")

    def check_stock(self, item):
        for i in self.items:
            if i.name == item.name:
                return i.quantity
        return f"{item.name} not found!"

    def update_stock(self, item_name, quantity):
        for item in self.items:
            if item.name == item_name:
                if item.quantity + quantity >= 0:
                    item.quantity += quantity
                    return f"Updated stock for {item.name}: {item.quantity}"
                return f"Error: Not enough stock to remove {abs(quantity)} items"
        return f"Error: {item_name} not found in inventory"

    def get_items(self):
        if not self.items:
            return "No items in inventory"
        return "\n".join(str(item) for item in self.items)
