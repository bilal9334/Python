import pytest
from vehicle import VehicleRegistry, Vehicle


def vehicle():
    v1 = Vehicle("Car", "BCY-210")
    v2 = Vehicle("Motorcycle", "MXZ-123")
    assert v1.vehicle_type
    assert v1.license_plate
    assert v2.vehicle_type
    assert v2.license_plate


def test_add_vehicle():
    vehicle_1 = Vehicle("Car", "BCY-210")
    vehicle_2 = Vehicle("Motorcycle", "MXZ-123")
    registry = VehicleRegistry()

    registry.add_vehicle(vehicle_1)
    registry.add_vehicle(vehicle_2)

    assert vehicle_1 in registry.vehicles
    assert vehicle_2 in registry.vehicles


def test_remove_vehicle():
    vehicle_1 = Vehicle("Car", "BCY-210")
    vehicle_2 = Vehicle("Motorcycle", "MXZ-123")
    registry = VehicleRegistry()

    registry.remove_vehicle(vehicle_1)
    registry.remove_vehicle(vehicle_2)

    assert vehicle_1 not in registry.vehicles
    assert vehicle_2 not in registry.vehicles


def non_existent_vehicle_cannot_be_removed():
    vehicle_1 = Vehicle("Car", "BCY-210")
    vehicle_2 = Vehicle("Motorcycle", "MXZ-123")
    registry = VehicleRegistry()

    registry.add_vehicle(vehicle_1)
    result = registry.remove_vehicle(vehicle_2)
    assert vehicle_2 not in registry.vehicles
    assert result == "Vehicle not found!"


def test_find_vehicle():
    vehicle_1 = Vehicle("Car", "BCY-210")
    vehicle_2 = Vehicle("Motorcycle", "MXZ-123")
    registry = VehicleRegistry()
    registry.add_vehicle(vehicle_1)
    registry.add_vehicle(vehicle_2)

    result_found_1 = registry.find_vehicle("BCY-210")
    result_found_2 = registry.find_vehicle("MXZ-123")
    result_not_found = registry.find_vehicle("AJX-038")

    assert result_found_1 == "Vehicle found!"
    assert result_found_2 == "Vehicle found!"
    assert result_not_found == "Vehicle not found!"


def test_list_vehicles():
    vehicle_1 = Vehicle("Car", "BCY-210")
    vehicle_2 = Vehicle("Motorcycle", "MXZ-123")
    registry = VehicleRegistry()
    registry.add_vehicle(vehicle_1)
    registry.add_vehicle(vehicle_2)
    assert registry.list_vehicles() == ["Car", "Motorcycle"]
