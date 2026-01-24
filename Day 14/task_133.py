"""
Safely Access Attributes Using hasattr()
Create a class User with attributes name and email.
Create a function called print_user_info() that:
Takes an instance of User (or any object).
Checks whether it has the attributes name and email.
If those attributes exist, print their values.
Otherwise, print a message indicating the attribute is missing.
"""
class User:
    def __init__(self, name):
        self.name = name
        # self.email = email

def print_user_info(user):
    if hasattr(user, 'name'):
        print(f"Name: {user.name}")
    else:
        print("No 'name' attribute found.")

    if hasattr(user, 'email'):
        print(f"Email: {user.email}")
    else:
        print("No 'email' attribute found.")

# Example usage
user1 = User("Alice")
print_user_info(user1)
