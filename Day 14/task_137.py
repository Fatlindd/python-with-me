"""
Understand Object Identity Using id()
Write a program that:
Creates two variables with the same value.
Uses id() to compare their memory locations.
Modifies one of the variables and compares again.
The goal is to understand object identity, immutability, and how Python handles memory references.
"""
# Step 1: Assign same value to two variables
a = 100
b = 100

# Step 2: Print their ids
print("Before modification:")
print("id(a):", id(a))
print("id(b):", id(b))
print("a is b:", a is b)

# Step 3: Modify one variable
b += 1

# Step 4: Print their ids again
print("\nAfter modifying b:")
print("id(a):", id(a))
print("id(b):", id(b))
print("a is b:", a is b)  # Now False
