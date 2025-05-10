class Vehicle:
    # Class variable to track number of vehicles
    vehicle_count = 0

    def __init__(self, model, max_speed):
        self.model = model                  # Public attribute
        self._max_speed = max_speed          # Protected attribute
        Vehicle.vehicle_count += 1
        self.__vehicle_id = Vehicle.vehicle_count  # Private attribute (auto-incremented)

    def display_info(self):
        """Instance method to display vehicle info."""
        print(f"Model: {self.model}")
        print(f"Max Speed: {self._max_speed} km/h")
        print(f"Vehicle ID: {self.__vehicle_id}")

    @classmethod
    def get_vehicle_count(cls):
        """Class method to return the total number of vehicles."""
        return cls.vehicle_count

    @staticmethod
    def is_speeding(speed):
        """Static method to check if speed is greater than 100."""
        return speed > 100


class Truck(Vehicle):
    def __init__(self, model, max_speed, cargo_capacity):
        super().__init__(model, max_speed)
        self.cargo_capacity = cargo_capacity  # Additional attribute for Truck

    def display_info(self):
        """Override to include cargo capacity."""
        super().display_info()
        print(f"Cargo Capacity: {self.cargo_capacity} tons")


# Testing
v1 = Vehicle("Sedan", 120)
v2 = Vehicle("Coupe", 90)
t1 = Truck("Heavy Truck", 80, 15)

print("\nVehicle Info:")
v1.display_info()

print("\nTruck Info:")
t1.display_info()

print("\nTotal Vehicles Created:", Vehicle.get_vehicle_count())

print("\nIs 105 km/h speeding?", Vehicle.is_speeding(105))
print("Is 85 km/h speeding?", Vehicle.is_speeding(85))
