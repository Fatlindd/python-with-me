
"""
My pizzas, Your Pizzas

My Pizzas, Your Pizzas: Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
Add a new pizza to the original list.
Add a diﬀerent pizza to the list friend_pizzas.

Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
"""

# Original list
pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]

# Make a copy of the list
friend_pizzas = pizzas[:] # This creates a new independent copy

# Add new pizzas to each list
pizzas.append("Hawaiian")
friend_pizzas.append("Veggie Supreme")

# Print both lists to show they are separate
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(f"- {pizza}")

print("\nAre the two lists the same object?", pizzas is friend_pizzas)