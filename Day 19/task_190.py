"""
Merge Live User Config with System Defaults using update()

Requirements
You are building a configuration management system for a cloud platform. Each user’s configuration is partially stored
in a dictionary, while the system maintains a full dictionary of default settings.

You must:
    - Write a function merge_user_config(user_config: dict, default_config: dict) -> dict
    - Use the built-in update() method to:
        - Fill in missing values from the default config without overwriting existing user preferences.
    - Avoid mutating the original user_config (return a new dictionary instead).
"""
def merge_user_config(user_config: dict, default_config: dict) -> dict:
    # Start with a copy of default_config
    merged = default_config.copy()

    # Update with user_config, giving precedence to user values
    merged.update(user_config)

    return merged

# Example usage
default_config = {
   "theme": "light",
   "notifications": True,
   "language": "en-US",
   "autosave": False
}

user_config = {
   "theme": "dark",
   "autosave": True
}
final_config = merge_user_config(user_config, default_config)
print("Final Config:", final_config)