"""
Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
"""
favorite_numbers = {
    "Arta": 7,
    "Besim": 11,
    "Dren": 3,
    "Elira": 9,
    "Flamur": 5
}

# Print each person's favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")