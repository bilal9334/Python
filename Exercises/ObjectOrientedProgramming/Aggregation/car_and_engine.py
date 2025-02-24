class Engine:

    def start_engine(self):
        return "Engine Started"


class Car:

    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        if isinstance(self.engine, Engine):
            return f"{self.engine.start_engine()} | Car is ready to drive"
        return "Engine not available!"


if __name__ == '__main__':
    engine = Engine()
    car = Car(engine)
    print(car.drive())

    car2 = Car(None)
    print(car2.drive())
