class Engine:
    """Class to show the working of an Engine"""

    def start_engine(self):
        return "Engine started!"


class Car:
    """A car which delegates its working to Engine"""

    def __init__(self):
        self.engine = Engine()

    def engine_starting(self):
        return self.engine.start_engine()


if __name__ == '__main__':
    car = Car()
    print(car.engine_starting())
