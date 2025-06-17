class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100  # base fare per person is 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10  # 10% additional charges
        return base_fare + maintenance_charge

school_bus = Bus("School Volvo", 12, 50)

print(f"Vehicle Name: {school_bus.name}")
print(f"Total Fare: ₹{school_bus.fare()}")
