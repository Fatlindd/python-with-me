"""
Access Dynamic Attributes in a Class Using getattr()
Create a class Car with attributes like make, model, year, and color.
Write a function that accepts a Car instance and the name of the attribute as a string.
Use getattr() to dynamically retrieve the value of the attribute.
If the attribute does not exist, return a default message like "Attribute not found".
"""
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

def get_car_attribute(car_obj, attr_name):
    return getattr(car_obj, attr_name, "Attribute not found")

# Example usage
my_car = Car("Toyota", "Camry", 2020, "Blue")
print(get_car_attribute(my_car, "model"))       # Output: Camry
print(get_car_attribute(my_car, "year"))        # Output: 2020
print(get_car_attribute(my_car, "mileage"))     # Output: Attribute not found
