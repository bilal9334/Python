import pytest
from car import Car, ParkingLot


def test_car():
    car = Car("Toyota", "Corolla", 2020)
    assert car.make
    assert car.model
    assert car.year


def start_engine():
    car = Car("Toyota", "Corolla", 2020)
    assert car.start_engine() == "Vroom! The Toyota Corolla is now running!"


def test_add_car():
    parkinglot = ParkingLot(3)
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Volkswagen", "Golf", 2024)

    parkinglot.add_car(car1)
    parkinglot.add_car(car2)

    assert car1 in parkinglot.cars
    assert car2 in parkinglot.cars


def test_remove_car():
    parkinglot = ParkingLot(3)
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Volkswagen", "Golf", 2024)

    parkinglot.add_car(car1)
    parkinglot.add_car(car2)
    parkinglot.remove_car(car1)
    assert car1 not in parkinglot.cars


def test_lot_is_full():
    parkinglot = ParkingLot(3)
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Volkswagen", "Golf", 2024)
    car3 = Car("Honda", "Civic", 1998)
    car4 = Car("Hyundai", "Sonata", 2025)

    parkinglot.add_car(car1)
    parkinglot.add_car(car2)
    parkinglot.add_car(car3)
    result = parkinglot.add_car(car4)

    assert car4 not in parkinglot.cars
    assert result == "Parking lot full!"


def test_non_existent_car_cannot_be_removed():
    parkinglot = ParkingLot(3)
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Volkswagen", "Golf", 2024)
    car3 = Car("Honda", "Civic", 1998)
    car4 = Car("Hyundai", "Sonata", 2025)

    parkinglot.add_car(car1)
    parkinglot.add_car(car2)
    parkinglot.add_car(car3)
    result = parkinglot.remove_car(car4)

    assert car4 not in parkinglot.cars
    assert result == "Car not found!"


def test_list_cars():
    garage = ParkingLot(3)
    garage.add_car(Car("Toyota", "Corolla", 2020))
    garage.add_car(Car("Volkswagen", "Golf", 2024))
    assert garage.list_cars() == ["Corolla", "Golf"]


def test_find_car():
    parkinglot = ParkingLot(2)
    car1 = Car("Honda", "Civic", 1998)
    car2 = Car("Nissan", "Skyline", 2000)
    parkinglot.add_car(car1)
    parkinglot.add_car(car2)

    result_found = parkinglot.find_car("Nissan", "Skyline")
    result_not_found = parkinglot.find_car("Toyota", "Supra")
    assert result_found == "Car found!"
    assert result_not_found == "Car not found!"
