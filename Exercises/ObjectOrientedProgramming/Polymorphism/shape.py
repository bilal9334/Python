import math


class Shape:

    def calculate_area(self):
        return NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calculate_area(self):
        return self._width * self._length


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return math.pi * self._radius ** 2


if __name__ == '__main__':
    shapes = [Rectangle(5, 3), Circle(4)]
    for shape in shapes:
        print(f"Area: {shape.calculate_area():.2f}")
