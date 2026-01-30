"""
Use property() to Encapsulate Access to an Internal Attribute
You are asked to build a Circle class that:
Takes the radius of a circle during initialization.
Provides:
A getter method to access the area as a property.
A getter and setter for radius using the property() built-in function.
Automatically updates the area when the radius changes.
"""
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    def get_area(self):
        return 3.1416 * self._radius * 2

    radius = property(get_radius, set_radius)
    area = property(get_area)

# Usage
c = Circle(5)
print("Radius:", c.radius)
print("Area:", c.area)

c.radius = 10
print("Updated Radius:", c.radius)
print("Updated Area:", c.area)

