from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass
class BMW(Vehicle):
    def start_engine(self):
        return "BMW engine started with a roar!"

    def accelerate(self):
class Ferrari(Vehicle):
    def start_engine(self):
        return "Ferrari engine started with a thunder!"

    def accelerate(self):
        return "Ferrari accelerates to 100 km/h in 3.9 seconds!"

def test_drive(vehicle):
    print(vehicle.start_engine())
    print(vehicle.accelerate())

bmw_car = BMW()
ferrari_car = Ferrari()

print("Testing BMW:")
test_drive(bmw_car)

print("\nTesting Ferrari:")
test_drive(ferrari_car)
