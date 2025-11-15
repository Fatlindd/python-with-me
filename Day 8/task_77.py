"""
Number Served: Start with your program from Task 75. Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then
change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served. Call this
method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call
this method with any number you like that could represent how many customers were served in, say, a day of business.
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name, cuisine type, and default number served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # Default value

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine."""
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Announce the restaurant is open."""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >=0:
            self.number_served = number
        else:
            print("Number of customers cannot be negative.")

    def increment_number_served(self, additional_number):
        """Add to the number of customers served."""
        if additional_number > 0:
            self.number_served += additional_number
        else:
            print("Increment must be positive.")

# Create an instance
restaurant = Restaurant("Sushi Central", "Japanese")

# Display initial state
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"Customers served: {restaurant.number_served}")

# Modify and display update values
restaurant.number_served = 25
print(f"Update customers served: {restaurant.number_served}")

# Using increment_number_served()
restaurant.increment_number_served(5)
print(f"After increment: {restaurant.number_served}")