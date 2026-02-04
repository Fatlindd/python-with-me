"""
Validate and Log Data Types Using type()

Requirements
1. Create a list with mixed data types (e.g., string, int, float, list, dict).
2. Iterate over the list and use type() to:
    - Print the value.
    - Print its data type.
3. Add conditional logic:
    - If the type is str, print "This is a string".
    - If the type is int, print "This is an integer".
    - Otherwise, print "Other type".
"""
data = ["Python", 42, 3.14, [1, 2, 3], {"name": "Alice"}]

for item in data:
    print(f"Value: {item}")
    print(f"Type: {type(item)}")

    if type(item) is str:
        print("This is a string.\n")
    elif type(item) is int:
        print("This is an integer.\n")
    else:
        print("Other type.\n")
