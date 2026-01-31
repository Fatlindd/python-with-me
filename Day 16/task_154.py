"""
Use range() to Generate a Custom Multiplication Table
Write a Python function named generate_table() that:
Accepts two arguments: number (the base of the table) and limit (how many multiples to generate).
Uses the range() function to loop from 1 up to and including limit.
Returns a list of strings formatted as: "number x i = result".
"""
def generate_table(number, limit):
    result = []
    for i in range(1,limit + 1):
        result.append(f"{number} x {i} = {number * i}")
    return result

# Example usage
table = generate_table(5, 10)
for line in table:
    print(line)