"""
You’re building a backend script to validate form submissions. Each submission comes in as a dictionary with several
fields: 'name', 'email', 'phone', 'message'. Your job is to ensure all required fields are filled in before accepting
the form. Use the built-in all() function to quickly check if all fields are non-empty (i.e., truthy).
"""
def is_valid_submission(form_data):
    # Check if all values in the form_data are truthy (non-empty)
    return all(form_data.values())

# Test forms
form_1 = {
    "name": "Alice",
    "email": "alice@example.com",
    "phone": "123-456-7890",
    "message": "I'm interested in your services."
}

form_2 = {
    "name": "Bob",
    "email": "",
    "phone": "555-1234",
    "message": "Contact me please."
}

print(is_valid_submission(form_1))
print(is_valid_submission(form_2))