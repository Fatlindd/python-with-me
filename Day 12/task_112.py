"""
You’re building a form validation utility. Users submit a form with three fields:
name (string)
email (string)
age (integer or string)

Your task is to:
1. Write a function that uses bool() to check if each field is filled in.
2. Return a message that tells whether the form is complete or missing data.
3. Print the boolean result of each field using bool().
"""
def validate_form(form):
    print("Checking field values...")
    for field, value in form.items():
        print(f"{field.capitalize()} valid? {bool(value)}")

    if all(bool(value) for value in form.values()):
        return "Form is complete!"
    else:
        return "Form is missing some information."

# Example data
form_data = {
   "name": "Fatlind",
   "email": "Fatlind@example.com",
   "age": ""  # Simulates user forgot to enter age
}

print(validate_form(form_data))

