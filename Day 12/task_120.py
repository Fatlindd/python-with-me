"""
You are designing a basic class called UserProfile to manage user information. Your tasks:
Define a class with attributes like username, email, and bio.
Allow users to delete the bio attribute using the delattr() function.
After deletion, try accessing the deleted attribute and handle the error.
"""
class UserProfile:
   def __init__(self, username, email):
       self.username = username
       self.email = email
       self.bio = "This user hasn't written a bio yet."

# Create an instance of UserProfile
user = UserProfile("midlevel_dev", "mid@example.com")

# Print attributes before deletion
print("Before deletion:", user.__dict__)

# Delete the 'bio' attribute dynamically
delattr(user, 'bio')

# Check attributes after deletion
print("After deletion:", user.__dict__)

# Try to access the deleted attribute safely
try:
   print(user.bio)
except AttributeError:
   print("The 'bio' attribute has been deleted and is no longer available.")
