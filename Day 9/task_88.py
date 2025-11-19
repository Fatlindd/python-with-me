"""
Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a
list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.
"""
import random

def get_random_ticket(items, size=4):
   return random.sample(items, size)

def run_lottery_simulation():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
    my_ticket = [4, 'B', 7, 'C']  # You can customize this

    count = 0
    while True:
        drawn_ticket = get_random_ticket(items)
        count += 1

        if set(drawn_ticket) == set(my_ticket):
            break

    print(f"🏆 It took {count} tries to win the lottery with ticket: {my_ticket}")

run_lottery_simulation()