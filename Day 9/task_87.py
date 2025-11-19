"""
Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters
from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
"""
import random

# Define the pool of numbers and letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 unique items
winning_ticket = random.sample(lottery_items, 4)

# Display the result
print("🎉 Any ticket matching these 4 numbers or letters wins a prize:")
print("Winning tickets: ", winning_ticket)


# lottery.py
class Lottery:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

    def draw_winning_ticket(self, count=4):
        return random.sample(self.items, count)

"""
# main.py
from lottery import Lottery

lotto = Lottery()
ticket = lotto.draw_winning_ticket()

print("🎉 Any ticket matching these 4 numbers or letters wins a prize:")
print("Winning ticket:", ticket)
"""
