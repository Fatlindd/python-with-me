"""
Create a function named is_positive() that returns True if a number is greater than or equal to 0.
Use the built-in filter() function to filter out all negative numbers from a list of integers.
Convert the result of filter() into a list and print it.
"""
# Step 1: Define the filtering condition
def is_positive(number):
    return number > 0

# Step 2: Original list with positive and negative numbers
numbers = [-10, 5, 0, -3, 8, -2, 7]

# Step 3: Use filter to apply the condition
positive_numbers = list(filter(is_positive, numbers))

# Step 4: Output result
print("Filtered positive numbers: ", positive_numbers)