class Engine:

    def start(self):
        return "Engine Starting..."


class Wheel:

    def rotate(self):
        return "Wheel rotating..."


class FuelTank:

    def __init__(self, fuel):
        self._fuel = fuel

    def check_fuel(self):
        if self._fuel > 0:
            return "Fuel check passed"
        else:
            return "Not enough fuel"


class Car:

    def __init__(self, engine, wheel, fuel_tank):
        self.engine = engine
        self.wheel = wheel
        self.fuel_tank = fuel_tank

    def drive(self):
        fuel_status = self.fuel_tank.check_fuel()
        if fuel_status == "Fuel check passed":
            return f"{self.engine.start()} {self.wheel.rotate()}"
        else:
            return fuel_status


if __name__ == '__main__':
    engine = Engine()
    wheel = Wheel()
    fuel_tank = FuelTank(-1)

    car = Car(engine, wheel, fuel_tank)
    print(car.drive())
