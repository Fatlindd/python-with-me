"""
Ask the user to input a function definition (as a string).
Use exec() to define that function dynamically.
Call the defined function afterward to verify it works.
The function must have a specific name like greet() and return a string.
"""
# Step 1: Prompt user for a function definition
print("Define a function named greet(). Example:\n\ndef greet():\n    print('Hello, world!')\n")
user_code = ""

print("Enter your function definition line-by-line. Type 'END' to finish:")

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    user_code += line + "\n"

# Step 2: Execute the user-defined function
try:
    exec(user_code)  # Dynamically defines the function
    print("Function defined successfully.")

    # Step 3: Call the function
    greet()
except Exception as e:
    print(f"Error during execution: {e}")


