"""
Manage Dynamic Configuration Overrides with pop()

Requirements
You are working on a dynamic configuration system for a microservices platform.

Your task is to:
    - Write a function remove_sensitive_keys() that removes sensitive keys from a config dictionary before it's sent to
      client-side logs or frontend APIs.
    - The sensitive keys to remove are stored in a list: ["password", "token", "api_key"].
    - Use the built-in pop() method to safely remove the key from the dictionary and log the removed values.
    - Avoid raising a KeyError if a sensitive key does not exist.
"""
def remove_sensitive_keys(config, sensitive_keys):
    redacted = {}
    for key in sensitive_keys:
        redacted_value = config.pop(key, None)
        if redacted_value is not None:
            redacted[key] = redacted_value
    return config, redacted

# Example usage
config = {
   "host": "localhost",
   "port": 8000,
   "user": "admin",
   "password": "s3cr3t",
   "token": "abcd1234"
}

sensitive_keys = ["password", "token", "api_key"]
clean_config, removed_data = remove_sensitive_keys(config, sensitive_keys)

print("Sanitized Config:", clean_config)
print("Redacted Data:", removed_data)