class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"Vroom! The {self.make} {self.model} is now running!"


class Garage:

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def list_cars(self):
        return [car.model for car in self.cars]
