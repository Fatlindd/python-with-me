"""
You're working on a backend validation system where user data is submitted via form. You want to detect if any of the
required fields are missing so you can show a warning or prevent submission.
You will use Python’s built-in any() function to help detect if at least one field is empty, without writing repetitive
if conditions.
"""
def has_missing_fields(data):
    # Return True if any field is empty
    return any(value == '' for value in data.values())

# Example usage
form_1 = {
    "name": "Liam",
    "email": "liam@example.com",
    "phone": "123-456-7890",
    "message": "Please call me."
}

form_2 = {
    "name": "John",
    "email": "",
    "phone": "321-456-7890",
    "message": "Need help."
}

print(has_missing_fields(form_1))
print(has_missing_fields(form_2))
