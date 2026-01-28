"""
Validate Password Length in a Registration Form
Create a simple validate_password(password) function.
The password should be at least 8 characters long.
If the password is valid, return "Password is valid".
If not, return "Password must be at least 8 characters long".
Use the built-in len() function to perform the check.
"""
def validate_password(password):
    if len(password) >= 8:
        return "Password is valid"
    else:
        return "Password must be at least 8 characters long."

# Example usage
print(validate_password("abc123"))
print(validate_password("securepass"))