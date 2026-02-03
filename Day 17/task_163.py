"""
Use str() to Convert Various Data Types into Readable Strings

Requirements
1. Create a Python script that defines:
    - An integer (age = 30)
    - A float (balance = 1050.75)
    - A list of items (items = ['apple', 'banana', 'cherry'])
    - A boolean (is_logged_in = True)
2. Convert each of these variables to a string using the str() function.
3. Concatenate them into a meaningful sentence.
4. Print the final result.
"""
age = 30
balance = 1050.75
items = ['apple', 'banana', 'cherry']
is_logged_in = True

# Convert all values to string using str()
sentence = f"User info: Age - {str(age)}, Balance - {str(balance)}, Items - {str(items)}, is_logged_in - {str(is_logged_in)}"
print(sentence)