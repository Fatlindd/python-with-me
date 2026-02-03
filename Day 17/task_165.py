"""
Inherit Behavior Using super() in a Method Overriding Scenario

Requirements
1. Create a base class Vehicle with an __init__ method that sets brand and year, and a method start().
2. Create a child class Car that:
    - Inherits from Vehicle
    - Adds an attribute model
    - Overrides the start() method but still calls the parent start() using super()
3. Instantiate a Car object and call the start() method to observe combined behavior.
"""
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print(f"{self.brand} ({self.year}) is starting...")

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year) # Call Vehicle's constructor
        self.model = model

    def start(self):
        super().start()  # Call Vehicle's start()
        print(f"{self.model} engine is now running.")

# Instantiate and test
my_car = Car("Mercedes", 2023, "E-Class")
my_car.start()