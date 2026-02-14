"""
Implement a LIFO-based Configuration Rollback System

Requirements
You are managing a runtime configuration system that allows dynamic updates and needs rollback support.
    - You must implement a function rollback_last_config_change(config_history) that:
        - Uses Python’s built-in popitem() to remove the most recently added key-value pair from the dictionary.
        - Returns the updated config and the rolled-back key-value pair.
    - Simulate 3 configuration changes and then perform a rollback.
"""
def rollback_last_config_change(config_history):
    try:
        key, value = config_history.popitem()
        print(f"Rolled back key: {key}, value: {value}")
        return config_history, (key, value)
    except KeyError:
        print("No configuration to rollback.")
        return config_history, None

# Simulate dynamic configuration updates
config = {}
config["feature_x_enabled"] = True
config["max_connections"] = 500
config["debug_mode"] = False

print("Config before rollback:", config)
config, rolled_back = rollback_last_config_change(config)

print("Config after rollback:", config)
print("Rolled Back Item:", rolled_back)