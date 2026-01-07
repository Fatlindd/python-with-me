"""
Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number
in a file. Write a separate program that reads in this value and prints the message “I know your favorite number!
It’s _____.”

You'll create two programs:
One that asks the user for their favorite number and saves it using JSON.
Another that reads the stored value and prints a friendly message like:
"I know your favorite number! It’s 7."
"""

# Program 1: Save the Favorite Number
import json

filename = 'favorite_number.json'
favorite_number = input("What is your favorite number? ")
with open(filename, 'w') as f:
   json.dump(favorite_number, f)
   print("Thanks! We'll remember your favorite number.")


# Program 2: Load the Favorite Number
try:
   with open(filename) as f:
       number = json.load(f)
       print(f"I know your favorite number! It’s {number}.")
except FileNotFoundError:
   print("No favorite number found. Run the other program first.")