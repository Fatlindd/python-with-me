"""
Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""

# Pizza Toppings
print("Enter 'quit' when you're done.")

while True:
   topping = input("Enter a pizza topping: ")

   if topping.lower() == 'quit':
       print("Finished making your pizza!")
       break
   else:
       print(f"Adding {topping} to your pizza.")