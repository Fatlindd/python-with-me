"""
You are building a simple scientific calculator that supports complex number addition. Your tasks:
Create two complex numbers using the built-in complex() function.
Perform addition between them.
Display the real and imaginary parts separately.
Let the user optionally input real and imaginary parts to generate their own complex number.
"""
# Creating complex numbers using real and imaginary parts
num1 = complex(2, 3)     # 2 + 3j
num2 = complex(1.5, -1)  # 1.5 - 1j

# Performing addition
result = num1 + num2

# Display the result and its parts
print("Number 1:", num1)
print("Number 2:", num2)
print("Sum:", result)
print("Real Part:", result.real)
print("Imaginary Part:", result.imag)
