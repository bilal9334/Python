class WaterTank:

    def __init__(self):
        self._current_water_level = 1000
        self._total_water_level = 8000

    def check_water(self):
        if self._current_water_level < 2000:
            return "Low water! Refill needed"
        return f"Water level is sufficient: {self._current_water_level}ml"

    def fill(self):
        self._current_water_level = self._total_water_level
        return "Water Tank refilled to maximum capacity"


class Grinder:

    def grind_beans(self):
        return "Grinding coffee beans..."


class Heater:

    def __init__(self, water_tank):
        self.water_tank = water_tank

    def heat_water(self):
        if self.water_tank._current_water_level > 1000:
            self.water_tank._current_water_level -= 500
            return "Heating Water"
        else:
            return "Not enough water to heat"


class CoffeeMachine:

    def __init__(self):
        self.water_tank = WaterTank()
        self.grinder = Grinder()
        self.heater = Heater(self.water_tank)

    def make_coffee(self):
        if self.water_tank._current_water_level < 1000:
            return "Error: Not enough to make coffee"

        grind = self.grinder.grind_beans()
        heat = self.heater.heat_water()
        return f"{grind} {heat} Coffee is ready!"


if __name__ == '__main__':

    coffee = CoffeeMachine()
    print(coffee.water_tank.check_water())
    print(coffee.water_tank.fill())
    print(coffee.water_tank.check_water())

    print(coffee.make_coffee())
    print(coffee.make_coffee())
