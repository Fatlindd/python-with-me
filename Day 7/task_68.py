"""
Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one
parameter that collects as many items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a diﬀerent number of arguments each time.
"""
def make_sandwich(*items):
   """Build a sandwich with any number of ingredients."""
   print("\nMaking a sandwich with the following ingredients:")
   for item in items:
       print(f" - {item}")
   print("Your sandwich is ready!\n")

# Call the function with different numbers of items
make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("peanut butter", "banana")
make_sandwich("grilled chicken", "cheddar cheese", "bacon", "avocado", "spinach")