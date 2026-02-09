"""
Use clear() to Reset Cached Configuration Data

Requirements
You are building a configuration loader system that:
    - Caches settings from multiple config files (e.g., JSON or ENV) in a dictionary.
    - Needs a reset() function that clears the entire config cache when required (e.g., during testing,
    reinitialization, or when a new user logs in).

Your task:
1. Create a class ConfigCache with the following:
    - A config_data dictionary attribute (to simulate loaded config).
    - A method load_sample_data() that fills the dictionary with dummy config values.
    - A method reset() that clears all config entries using clear().
2. Demonstrate its use by:
    - Loading data.
    - Printing the cache.
    - Resetting it.
    - Printing again to confirm it's empty.
"""
class ConfigCache:
    def __init__(self):
        self.config_data = {}

    def load_sample_data(self):
        self.config_data = {
            "host": "localhost",
            "port": 8080,
            "debug": True,
            "api_key": "XYZ-12345"
        }

    def reset(self):
        self.config_data.clear()

# Demo
cache = ConfigCache()
cache.load_sample_data()
print("Before reset: ", cache.config_data)

cache.reset()
print("After reset: ", cache.config_data)