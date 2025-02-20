class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return "Brand: {0.brand}, Model: {0.model}".format(self)


class Car(Vehicle):

    def __init__(self, brand, model, seats):
        super().__init__(brand, model)  # Calling parent class constructor
        self.seats = seats # Adding new attribute

    def display(self):
        return "Brand: {0.brand}, Model: {0.model}, Seat: {0.seats}".format(self)


if __name__ == '__main__':
    my_car = Car("Toyota", 1997, 4)
    print(my_car.display())
