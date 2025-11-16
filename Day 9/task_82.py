"""
Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called
upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an
electric car with a default battery size, call get_range() once, and then call get_range() a second time after
upgrading the battery. You should see an increase in the car’s range.
"""

# Battery Class
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range_km = 240
        elif self.battery_size == 65:
            range_km = 400
        print(f"This car can go about {range_km} km on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65-kWh")
        else:
            print("Battery is already upgraded.")


# Car class (base)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"


# ElectricCar class inherits from Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Create an ElectricCar and upgrade its battery
my_tesla = ElectricCar("tesla", "model", 2019)
print(my_tesla.get_description())

# Before upgrade
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrade and check again
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
