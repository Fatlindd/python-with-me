"""
Three Restaurants: Start with your class from Exercise 74. Create three diﬀerent instances from the class, and call
describe_restaurant() for each instance.
"""
class Restaurant:
   def __init__(self, restaurant_name, cuisine_type):
       """Initialize restaurant name and cuisine type."""
       self.restaurant_name = restaurant_name
       self.cuisine_type = cuisine_type


   def describe_restaurant(self):
       """Describe the restaurant."""
       print(f"\nRestaurant Name: {self.restaurant_name}")
       print(f"Cuisine Type: {self.cuisine_type}")


   def open_restaurant(self):
       """Indicate that the restaurant is open."""
       print(f"{self.restaurant_name} is now open!")

# Create three instances
restaurant1 = Restaurant("Bella Italia", "Italian")
restaurant2 = Restaurant("Dragon Wok", "Chinese")
restaurant3 = Restaurant("La Taqueria", "Mexican")

# Call describe_restaurant() for each
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()