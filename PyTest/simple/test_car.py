import pytest
from car import Car, Garage


def test_car():
    car = Car("Toyota", "Corolla", 2020)
    assert car.make
    assert car.model
    assert car.year


def start_engine():
    car = Car("Toyota", "Corolla", 2020)
    assert car.start_engine() == "Vroom! The Toyota Corolla is now running!"


def test_add_car():
    garage = Garage()
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Volkswagen", "Golf", 2024)

    garage.add_car(car1)
    garage.add_car(car2)

    assert car1 in garage.cars
    assert car2 in garage.cars


def test_list_cars():
    garage = Garage()
    garage.add_car(Car("Toyota", "Corolla", 2020))
    garage.add_car(Car("Volkswagen", "Golf", 2024))
    assert garage.list_cars() == ["Corolla", "Golf"]
