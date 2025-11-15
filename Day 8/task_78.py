"""
Login Attempts: Add an attribute called login_attempts to your User class from Task 76. Write a method called
increment_login_attempts() that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts
to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure
it was reset to 0.
"""
class User:
    def __init__(self, first_name, last_name, age, location):
        """Initialize user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back!")

    def increment_login_attempts(self):
        """Increments login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0."""
        self.login_attempts = 0

# Creating multiple user instances
user1 = User("Emily", "Clark", 28, "New York")

# Simulate login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print current login attempts
print(f"\nLogin attempts: {user1.login_attempts}")

# Reset login attempts
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")