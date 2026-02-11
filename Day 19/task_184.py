"""
Build a Safe User Profile Lookup System Using dict.get()

Requirements
You are building a backend for a user management system where user profiles are stored in a dictionary.
Your goal is to:
1. Safely retrieve user information using the get() method.
2. Handle missing keys gracefully by returning fallback values.
3. Avoid KeyError exceptions that may arise from direct access.
4. Use get() in a chained expression to calculate derived data.
"""
# Simulated user profile database
user_profiles = {
    "jane_doe": {"email": "jane@example.com", "age": 29},
    "john_smith": {"email": "john@example.com"}
}

def get_user_email(username):
    # Safe retrieval with fallback
    profile = user_profiles.get(username)
    if profile:
        return profile.get("email", "Email not provided")
    return "User not found"

def get_user_age(username):
    # Safe retrieval with chained get
    return user_profiles.get(username, {}).get("age", "Age not provided")

# Test cases
print(get_user_email("jane_doe"))
print(get_user_email("unknown_user"))
print(get_user_age("jane_smith"))