"""
Detect Configuration Key Mismatches Using keys()

Requirements
You are tasked with creating a diagnostic function that compares two configuration dictionaries:
    - expected_config: contains all required keys for a system to operate.
    - actual_config: contains the current keys loaded into the system.

Your goal is to:
1. Use the keys() method to extract the key sets.
2. Identify any missing keys from the actual configuration.
3. Identify any unexpected keys that should not be there.
4. Print a structured report showing both types of mismatches.
"""
def validate_config(expected_config, actual_config):
    expected_keys = expected_config.keys()
    actual_keys = actual_config.keys()

    missing_keys = expected_keys - actual_keys
    extra_keys = actual_keys - expected_keys

    if missing_keys:
        print("Missing keys:", missing_keys)
        for key in missing_keys:
            print(f" - {key}")

    if extra_keys:
        print("Extra keys:", extra_keys)
        for key in extra_keys:
            print(f" - {key}")

    if not missing_keys and not extra_keys:
        print("Configuration keys match perfectly.")

# Example usage
expected_config = {
   "host": "localhost",
   "port": 5432,
   "user": "admin",
   "password": "secret"
}


actual_config = {
   "host": "localhost",
   "port": 5432,
   "username": "admin",
   "timeout": 60
}

validate_config(expected_config, actual_config)