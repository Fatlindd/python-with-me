"""
Validate Permissions System Using issubclass()
Define a base class called User.
Create two subclasses: Admin and Guest.
Write a function has_admin_privileges(cls) that:
Accepts a class (not an instance).
Returns True if the class is a subclass of Admin.
Otherwise, returns False.
Test the function by passing different class references to it, such as Admin, Guest, and User.
"""
# Base class
class User:
    pass

# Subclasses
class Admin(User):
    pass

class Guest(User):
    pass

# Function using issubclass
def has_admin_privileges(cls):
    if not isinstance(cls, type):
        raise TypeError("Expected a class, not an instance.")
    return issubclass(cls, Admin)

# Test cases
print(has_admin_privileges(Admin))   # True
print(has_admin_privileges(Guest))   # False
print(has_admin_privileges(User))    # False