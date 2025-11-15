"""
Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other
attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of
the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.Create
several instances representing diﬀerent users, and call both methods for each user.
"""
class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back!")

# Creating multiple user instances
user1 = User("Emily", "Clark", 28, "New York", "Designer")
user2 = User("Liam", "Nguyen", 35, "San Francisco", "Software Engineer")
user3 = User("Fatima", "Hassan", 22, "Dubai", "Marketing Specialist")

# Calling methods for each user
users = [user1, user2, user3]
for user in users:
    user.describe_user()
    user.greet_user()