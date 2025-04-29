# 27. Create a class Vehicle:
# -Public attribute: model
# -Protected attribute: max_speed
# -Private attribute: vehicle_id (auto-incremented)
# -Instance method display_info() to show vehicle info
# -Class method get_vehicle_count() to return total vehicles
# -Static method is_speeding(speed) → return True if speed > 100
# -Class variable for vehicle count
#     -Create a subclass Truck:
# -Adds cargo_capacity attribute
# -Overrides display_info() to include cargo capacity
import uuid

class Vehicle:
    vehicle_count = 0
    def __init__(self, model, max_speed):
        self.__id = None #private
        self.model = model  #public
        self._max_speed = max_speed #protected
        Vehicle.vehicle_count =Vehicle.vehicle_count+1
    def set_vehicle_id(self):
        self.__id = uuid.uuid4()
    def get_vehicle_id(self):
        return self.__id
    def display_info(self):
        self.set_vehicle_id()
        print(f"Vehicle Id: {self.__id}, Vehicle model: {self.model}, Vehicle max speed: {self._max_speed}")

    @staticmethod
    def is_speeding(speed):
        return speed >100
    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count

    @property
    def max_speed(self):
        return self._max_speed

class Truck(Vehicle):
    def __init__(self,  model, max_speed,cargo_capacity):
        super().__init__(model, max_speed)
        self.cargo_capacity = cargo_capacity
    def display_info(self):
        super().display_info()
        print(f"Cargo capacity: {self.cargo_capacity}")

vehicle1 = Vehicle("Toyoto Corolla",120)
vehicle1.display_info()
vehicle2 = Vehicle("Honda Civic", 90)
vehicle2.display_info()
truck1 = Truck("Volvo FH", 80 , 3000)
truck1.display_info()

print("current vehicle count: ", Vehicle.get_vehicle_count())
truck2 = Truck("Volvo FH2", 90 , 4000)
truck2.display_info()
print("current vehicle count: ", Vehicle.get_vehicle_count())
print(Vehicle.is_speeding(110))
print(Vehicle.is_speeding(70))

print(vehicle1.model)
print(vehicle1._max_speed)
print(vehicle1.get_vehicle_id())
