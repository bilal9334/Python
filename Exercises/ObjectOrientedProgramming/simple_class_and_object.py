class Car:
    """Simple class to show information of a car"""

    wheels = 4  # Class Attribute

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year} - Wheels: {Car.wheels}")


if __name__ == '__main__':
    my_car_1 = Car("Toyota", "Corolla", 2022)
    my_car_1.display_info()
    my_car_2 = Car("Honda", "Civic", 1997)
    my_car_2.display_info()
