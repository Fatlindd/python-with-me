"""
User Dictionary: The remember_me.py example only stores one piece of information, the username. Expand this example
by asking for two more pieces of information about the user, then store all the information you collect in a
dictionary. Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). Print a
summary showing exactly what your program remembers about the user.

Enhance the remember_me.py example by storing more than just the username.
"""
import json

filename = 'user_info.json'

try:
    with open(filename, 'r') as f:
        user_info = json.load(f)
        print("Welcome back!")
        print(f"We remember you: {user_info['first_name']} {user_info['last_name']}, age {user_info['age']}")
except FileNotFoundError:
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    age = input("What is your age? ")

    user_info = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    }

    with open(filename, 'w') as f:
        json.dump(user_info, f)

    print("Thank you! We've saved your info for next time.")