"""
Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class. Add
an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so
on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of
Admin, and call your method.
"""
# Parent class
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

# Child class
class Admin(User):
    def __init__(self, first_name, last_name, email, location):
        super().__init__(first_name, last_name, email, location)
        self.privileges = [
            "can add post",
           "can delete post",
           "can ban user",
           "can view analytics",
           "can reset passwords"
        ]

    def show_privileges(self):
        print(f"\nAdmin Privileges: for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Create instance and call methods
admin_user = Admin("Alice", "Johnson", "alice@example.com", "New York")
admin_user.describe_user()
admin_user.greet_user()
admin_user.show_privileges()