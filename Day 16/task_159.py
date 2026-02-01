"""
Dynamically Update Object Attributes Using setattr()

Requirements
Create a simple User class with attributes name and email.
Use the built-in setattr() function to dynamically:
- Update an existing attribute (like email).
- Add a new attribute (like age) at runtime.
- Print the updated attributes to verify changes.
"""
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Create an instance of User
user1 = User("John Doe", "john@example.com")

# Use setattr() to update the email
setattr(user1, "email", "john.doe@newdomain.com")

# Use setattr() to add a new attribute 'age'
setattr(user1, "age", 30)

# Print results
print(f"Name: {user1.name}")
print(f"Email: {user1.email}")
print(f"Age: {user1.age}")