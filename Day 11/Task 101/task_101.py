"""
Favorite Number Remembered: Combine the two programs you wrote in previous exercises into one file. If the number is
already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in
a file. Run the program twice to see that it works.
"""
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
        print(f"I know your favorite number! It's {favorite_number}")
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print("Thanks! We'll remember your favorite number!")