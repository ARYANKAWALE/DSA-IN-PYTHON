class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car +=1

    def getBrand(self):
        return self.brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        print("This car uses petrol")
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        print("This car uses electricity")

my_car = Car("ferrari","enzo")
print(my_car.full_name())
my_car.fuel_type()

my_tesla = ElectricCar("tesla","model S","80 kWh")
print(my_tesla.getBrand())
my_tesla.fuel_type()
print(Car.total_car)