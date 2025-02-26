class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"Vroom! The {self.make} {self.model} is now running!"


class ParkingLot:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []

    def add_car(self, car):
        if len(self.cars) >= self.capacity:
            return "Parking lot full!"
        else:
            self.cars.append(car)
            return "Car parked!"

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            return "Car removed!"
        else:
            return "Car not found!"

    def list_cars(self):
        return [car.model for car in self.cars]

    def find_car(self, make, model):
        for car in self.cars:
            if car.model == model and car.make == make:
                return "Car found!"
        return "Car not found!"
