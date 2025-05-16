class Vehicle:
    vehicle_count = 0

    def __init__(self, model, max_speed):
        self.model = model
        self._max_speed = max_speed
        self.__vehicle_id = Vehicle.vehicle_count
        Vehicle.vehicle_count += 1

    def display_info(self):
        print(f"Vehicle ID: {self.__vehicle_id}, Model: {self.model}, Max Speed: {self._max_speed}")        

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count

    @staticmethod
    def is_speeding(speed):
        return speed > 100

class Truck(Vehicle):
    def __init__(self, model, max_speed, cargo_capacity):
        super().__init__(model, max_speed)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        super().display_info()
        print(f"Cargo Capacity: {self.cargo_capacity}") 


Vehicle1 = Vehicle("Toyota", 120)
Vehicle1.display_info()

Truck1 = Truck("Ford", 100, 1000)
Truck1.display_info()

print(Vehicle.is_speeding(120))

print(Vehicle.get_vehicle_count())











