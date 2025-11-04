"""
Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
"""
# Restaurant Seating
# Ask the user how many people are in their dinner group
group_size = input("How many people are in your dinner group? ")

# Convert the input string to an integer
group_size = int(group_size)

# Decide whether a table is ready or not
if group_size > 8:
   print("Sorry, you'll have to wait for a table.")
else:
   print("Great, your table is ready!")
