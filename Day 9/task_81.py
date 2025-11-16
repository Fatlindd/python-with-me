"""
Privileges: Write a separate Privileges class. The class should have one attribute, privileges.. Move the
show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new
instance of Admin and use your method to show its privileges.
"""
# User class (Base)
class User:
   def __init__(self, first_name, last_name, email, location):
       self.first_name = first_name
       self.last_name = last_name
       self.email = email
       self.location = location

   def describe_user(self):
       print(f"\nUser Profile:")
       print(f"Name: {self.first_name} {self.last_name}")
       print(f"Email: {self.email}")
       print(f"Location: {self.location}")

   def greet_user(self):
       print(f"Hello {self.first_name}, welcome back!")


# Privileges class
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "can add post",
                "can delete post",
                "can ban user",
                "can view analytics",
                "can reset passwords"
            ]
        self.privileges = privileges

    def show_privileges(self):
        print("\nAdmin Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")


# Admin class (inherits from User)
class Admin(User):
   def __init__(self, first_name, last_name, email, location):
       super().__init__(first_name, last_name, email, location)
       self.privileges = Privileges()  # Composition

# Creating an Admin and displaying privileges
admin_user = Admin("Alice", "Johnson", "alice@example.com", "New York")
admin_user.describe_user()
admin_user.greet_user()
admin_user.privileges.show_privileges()

