"""
Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called
roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
import random


class Die:
    def __init__(self, sides=6):
        def __init__(self, sides=6):
            self.sides = sides

        def roll_die(self):
            return random.randint(1, self.sides)

"""
# main.py
from dice import Die

# 6-sided die
print("Rolling a 6-sided die:")
six_sided_die = Die()
for _ in range(10):
   print(six_sided_die.roll_die(), end=' ')
print("\n")


# 10-sided die
print("Rolling a 10-sided die:")
ten_sided_die = Die(10)
for _ in range(10):
   print(ten_sided_die.roll_die(), end=' ')
print("\n")


# 20-sided die
print("Rolling a 20-sided die:")
twenty_sided_die = Die(20)
for _ in range(10):
   print(twenty_sided_die.roll_die(), end=' ')
print()
"""