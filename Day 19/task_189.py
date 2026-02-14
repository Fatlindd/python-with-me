"""
Implement Lazy Initialization for User Settings Using setdefault()

Requirements
You are building a user settings manager for a SaaS dashboard. Your system needs to:
    - Store user preferences in a dictionary.
    - Automatically initialize missing preferences with default values.
    - Use the built-in setdefault() method to:
        - Return the existing preference value if it exists.
        - If not, insert it with a default and return the default value.
    - Create a function called get_user_preference(settings: dict, key: str, default_value).
"""
def get_user_preference(settings: dict, key: str, default_value):
    # Set default if key doesn't exist and return the value
    return settings.setdefault(key, default_value)

# Example usage
user_settings = {
   "theme": "dark",
   "notifications": True
}
print("Before:", user_settings)

# Accessing an existing key
theme = get_user_preference(user_settings, "theme", "light")
print("Theme:", theme)

# Accessing a missing key, should insert with default
language = get_user_preference(user_settings, "language", "en-US")
print("Language:", language)

print("After:", user_settings)