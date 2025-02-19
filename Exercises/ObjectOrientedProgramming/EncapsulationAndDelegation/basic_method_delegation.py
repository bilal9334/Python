class Chef:
    """Simple class to show what the chef is doing"""

    def cook(self):
        return "Chef is cooking!"


class Restaurant:
    """Delegates cooking to a Chef"""
    def __init__(self):   # Restaurant uses Chef for delegation
        self.chef = Chef()

    def is_cooking(self):
        return self.chef.cook()  # Delegating cooking to Chef


if __name__ == '__main__':
    res = Restaurant()
    print(res.is_cooking())
