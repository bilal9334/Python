class Temperature:
    """Converts temperature from Celsius to Fahrenheit"""

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value >= 0:
            self._celsius = value
        else:
            print("Temperature cannot be below -273.15 celsius!")

    @property
    def fahrenheit(self):
        return (self._celsius * (9 / 5)) + 32


if __name__ == '__main__':
    temp = Temperature(25)
    print(temp.celsius)
    print(temp.fahrenheit)

    temp.celsius = -300
    print(temp.celsius)
