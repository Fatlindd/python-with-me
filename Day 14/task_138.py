"""
Interactive Profile Generator Using input()
Create a program that:
Prompts the user to enter their name, age, and profession using input().
Processes the input and formats it into a short profile description.
Displays a final summary with the collected data.
This task demonstrates how to collect, convert, and display user input properly.
"""
# Collect input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
profession = input("Enter your profession: ")

# Convert age to integer (with basic validation)
try:
   age = int(age)
except ValueError:
   print("Invalid age input. Please enter a number.")
   exit()

# Format and display the profile
print("\nProfile Summary:")
print(f"Hello, {name.title()}! You are a {age}-year-old {profession.lower()}.")