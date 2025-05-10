class Vehicle:
    vehicle_count = 0
    def __init__(self,model,max_speed):
        self.model = model
        self._max_speed = max_speed
        Vehicle.vehicle_count+=1
        self.__vehicle_id = Vehicle.vehicle_count


    def display_info(self):
        print(f"vehicle_ID:{self.__vehicle_id}")
        print(f"Model: {self.model}")
        print(f"Max Speed: {self._max_speed} km/h")

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
        print(f"Cargo Capacity: {self.cargo_capacity} tons")


v1 = Vehicle("Toyota Corolla", 120)
v2 = Vehicle("Honda Civic", 90)
t1 = Truck("Volvo FH", 80, 3000)

v1.display_info()
t1.display_info()

print(Vehicle.get_vehicle_count())
print(Vehicle.is_speeding(110))
print(Vehicle.is_speeding(70))