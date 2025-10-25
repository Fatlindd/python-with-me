"""
No Users: Add an if test to hello_admin.py to make sure the list of users is not empty. If the list is empty, print the message We need to find some users! Remove all of the usernames from your list, and make sure the correct message is printed.
"""
# Start with a non-empty list (optional for testing)
usernames = ["admin", "jaden", "emily", "michael", "sara"]

# Clear the list to simulate no users
# usernames = []

# Check if the list is empty
if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")