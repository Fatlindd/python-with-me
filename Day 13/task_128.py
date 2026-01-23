"""
Write a program that asks the user to input three numbers as strings.
Convert the string inputs into floating-point numbers using float().
Calculate and display the average of the three numbers.
"""
# Step 1: Prompt user for three numbers (as strings)
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

# Step 2: Convert strings to float
f1 = float(num1)
f2 = float(num2)
f3 = float(num3)

# Step 3: Calculate average
average = (f1 + f2 + f3) / 3

# Step 4: Display result
print(f"The average of the numbers is: {average}")
