"""
Python Module of the Week: One excellent resource for exploring the Python standard library is a site called Python
Module of the Week. Go to https://pymotw.com and look at the table of contents. Find a module that looks interesting
to you and read about it, perhaps starting with the random module.
"""
import random

items = ['apple', 'banana', 'cherry']
print(random.choice(items))       # Random item
print(random.randint(1, 100))     # Random integer
print(random.sample(items, 2))    # Random 2-item selection