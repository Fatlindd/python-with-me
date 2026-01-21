"""
Prompt the user to input a basic mathematical expression (e.g. "2 + 3 * 5").
Use eval() to evaluate and print the result.
The program should continue until the user types "exit".
Add basic validation to prevent code injection or misuse.
"""
def safe_eval(expression):
    # Allow only certain characters (very basic check)
    allowed_chars = "0123456789+-*/(). "
    if all(char in allowed_chars for char in expression):
        try:
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid expression. Only members and basic operators are allowed.")

print("Enter a math expression (type 'exit' to quit): ")
while True:
    user_input = input(">>> ")
    if user_input.lower() == "exit":
        break
    safe_eval(user_input)