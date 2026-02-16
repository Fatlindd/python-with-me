"""
Detect Duplicate Values in Dictionary Using values()

Requirements

You’re building a validation layer for a configuration management system. Sometimes, due to user misconfiguration or
API bugs, multiple keys in a dictionary might share the same value (which is not allowed in your system).
You must:
    - Write a function check_duplicate_values(data: dict) -> list
    - Use the built-in values() method to:
        - Extract all values from the dictionary.
        - Identify and return a list of duplicated values (if any).
    - Optimize for readability and performance.
"""
from collections import Counter

def check_duplicate_values(data: dict) -> list:
    value_list = list(data.values())
    duplicates = [item for item, count in Counter(value_list).items() if count > 1]
    return duplicates

# Example usage
config = {
   "server_1": "10.0.0.1",
   "server_2": "10.0.0.2",
   "server_3": "10.0.0.1",
   "server_4": "10.0.0.3",
   "server_5": "10.0.0.2",
}

dupes = check_duplicate_values(config)
print("Duplicated IPs:", dupes)
