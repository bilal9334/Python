class Vehicle:

    def __init__(self, vehicle_type, license_plate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate

    def __str__(self):
        return f"Vehicle - Type: {self.vehicle_type}, License Plate: {self.license_plate}"


class VehicleRegistry:

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            return "Vehicle removed!"
        else:
            return "Vehicle not found!"

    def find_vehicle(self, license_plate):
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate:
                return "Vehicle found!"
        return "Vehicle not found!"

    def list_vehicles(self):
        return [vehicle.vehicle_type for vehicle in self.vehicles]
