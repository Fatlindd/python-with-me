"""
Implement a Configuration Diff Tool Using items()

Requirements
You are maintaining an enterprise configuration management system. The configurations for applications are stored as
dictionaries. Your task is to:
1. Compare two configuration dictionaries (old_config and new_config).
2. Use the items() method to iterate through key-value pairs efficiently.
3. Identify:
    - Keys that have changed values.
    - Keys that are newly added.
    - Keys that have been removed.
The output should print a diff report showing differences between the two configurations.
"""
def diff_configs(old_config, new_config):
    old_keys = set(old_config)
    print(f"old_keys: {old_keys}")
    new_keys = set(new_config)
    print(f"new_keys: {new_keys}")

    for key, old_value in old_config.items():
        if key in new_config:
            if new_config[key] != old_value:
                print(f"Modified: {key} changed from {old_value} to {new_config[key]}")
        else:
            print(f"Removed: {key} was removed")

    for key, new_value in new_config.items():
        if key not in old_config:
            print(f"Added: {key} = {new_value}")

# Example usage
old_config = {
    "debug": False,
    "max_connections": 100,
    "timeout": 30
}

new_config = {
    "debug": True,
    "max_connections": 100,
    "timeout": 60,
    "region": "us-west-1"
}

diff_configs(old_config, new_config)