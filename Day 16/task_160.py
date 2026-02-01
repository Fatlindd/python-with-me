"""
Use slice() to Extract Portions of a List

Requirements:
Create a list of 10 numbers (1 through 10).
Use the built-in slice() function to:
 - Extract the first 5 elements.
 - Extract every second element.
 - Reverse the list using slicing.
 Print the results of each slicing operation.
"""
# Original list
numbers = list(range(1, 11))
print(numbers)

# Slice objects
first_five = slice(0, 5)
every_second = slice(0, None, 2)
reversed_slice = slice(None, None, -1)

# Apply slicing
print("First five numbers:", numbers[first_five])
print("Every second number:", numbers[every_second])
print("Reversed list:", numbers[reversed_slice])