"""
Clean and Convert User Input Using int()
Build a script that:
Asks the user to enter 3 numbers (they might include whitespace or be input as strings).
Cleans and converts each input to an integer using int().
Calculates the sum and average of the three numbers.
Outputs the result clearly.
This task helps the developer understand how int() works with string inputs and highlights its importance in input
validation and numerical operations.
"""
# Prompt user for three numbers (as strings)
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

try:
    # Clean and convert strings to integers
    n1 = int(num1.strip())
    n2 = int(num2.strip())
    n3 = int(num3.strip())

    total = n1 + n2 + n3
    average = (n1 + n2 + n3) / 3

    print(f"\nTotal: {total}")
    print(f"Average: {average:.2f}")
except ValueError:
    print("Please enter a valid integers number only.")
