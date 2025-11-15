"""
Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class. Either version of the class will work; just
pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method
that displays these flavors. Create an instance of IceCreamStand, and call this method.
"""
# Parent Class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open.")

# Child Class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mango", "Cookies and Cream"]

    def display_flavors(self):
        print(f"\nAvailable ice cream flavors at {self.restaurant_name}.")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance
ice_cream_shop = IceCreamStand("Sweet Treats")
ice_cream_shop.describe_restaurant()
ice_cream_shop.display_flavors()