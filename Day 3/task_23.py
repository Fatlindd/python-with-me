"""
Buﬀet: A buﬀet-style restaurant oﬀers only five basic foods. Think of five simple foods, and store them in a tuple. Use a for loop to print each food the restaurant oﬀers.

Try to modify one of the items, and make sure that Python rejects the change.

The restaurant changes its menu, replacing two of the items with diﬀerent foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
"""

# Original menu (tuple with 5 items)
menu = ("Rice", "Chicken", "Salad", "Soup", "Bread")

# Print the original menu using a for loop
print("Original buffet menu: ")
for item in menu:
    print(f"- {item}")

# Try to modify one item (this will cause an error if uncommented)
# menu[0] = "Steak"  # Tuples are immutable — this will raise TypeError

try:
    menu[0] = "Steak"
except TypeError as e:
    print(f"Error: {e}")

# Redefine the tuple with 2 changes
menu = ("Rice", "Steak", "Salad", "Fish", "Bread")

# Print the revised menu
print("\nRevised buffet menu: ")
for item in menu:
    print(f"- {item}")