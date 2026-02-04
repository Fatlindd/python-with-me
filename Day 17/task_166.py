"""
Convert a List of Employee Names to an Immutable Tuple

Requirements
1. Start with a list of employee names.
2. Convert the list to a tuple using the tuple() function.
3. Attempt to modify the tuple and handle the exception gracefully.
4. Print the original list, the resulting tuple, and the error message.
"""
employees_list = ["Alice", "Bob", "Charlie", "Diana"]

# Convert the list to a tuple
employees_tuple = tuple(employees_list)

print("Original List:", employees_list)
print("Converted Tuple:", employees_tuple)

# Try modifying the tuple (should raise an error)
try:
    employees_tuple[1] = "Ben"
except TypeError as e:
    print(f"Error: {e}")