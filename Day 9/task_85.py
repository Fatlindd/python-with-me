"""
Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module.
In a separate file, create an Admin instance and call show_privileges() to show that everything is still working
correctly.
"""
# user_module.py
class User:
   def __init__(self, first_name, last_name, email, location):
       self.first_name = first_name
       self.last_name = last_name
       self.email = email
       self.location = location

   def describe_user(self):
       print(f"User: {self.first_name} {self.last_name}")
       print(f"Email: {self.email}")
       print(f"Location: {self.location}")

   def greet_user(self):
       print(f"Hello, {self.first_name}!")


# admin_module.py
"""
from user_module import User

class Privileges:
   def __init__(self, privileges=None):
       if privileges is None:
           privileges = ["can add post", "can delete post", "can ban user"]
       self.privileges = privileges

   def show_privileges(self):
       print("Admin privileges:")
       for privilege in self.privileges:
           print(f" - {privilege}")

class Admin(User):
   def __init__(self, first_name, last_name, email, location):
       super().__init__(first_name, last_name, email, location)
       self.privileges = Privileges()



# main.py
from admin_module import Admin

admin_user = Admin("Elena", "Smith", "elena@example.com", "Berlin")
admin_user.privileges.show_privileges()
"""