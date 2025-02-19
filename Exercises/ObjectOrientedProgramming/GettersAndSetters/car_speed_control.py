class Car:
    """Controlling the speed of the car"""

    def __init__(self, speed=0):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if 0 < value < 200:
            self._speed = value
        else:
            print("Value shall be between 0 and 200!")

    def accelerate(self, value):
        self._speed += value

    def brake(self, value):
        self._speed -= value


if __name__ == '__main__':
    my_car = Car()
    print(my_car.speed)

    my_car.accelerate(100)
    print(my_car.speed)

    my_car.brake(30)
    print(my_car.speed)

    my_car.speed = 250
    my_car.speed = -200
