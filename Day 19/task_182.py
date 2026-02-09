"""
Use copy() to Create a Safe Snapshot of Runtime Configuration

Requirements
You’re building a service that dynamically updates configuration settings during runtime. You need to:
1. Create a RuntimeConfig class that holds a dictionary called settings.
2. Implement a method snapshot() that returns a shallow copy of the current config using copy().
3. Demonstrate that modifying the snapshot does not affect the original dictionary (except for nested mutable values).
4. Explain potential pitfalls of copy() in deeply nested structures.
"""
class RuntimeConfig:
    def __init__(self):
        self.settings = {
            "debug": True,
            "timeout": 30,
            "features": {"beta": False, "dark_mode": True},
        }

    def snapshot(self):
        return self.settings.copy()

# Create instance and take snapshot
config = RuntimeConfig()
config_snapshot = config.snapshot()

# Modify snapshot
config_snapshot["timeout"] = 60
config_snapshot["features"]["dark_mode"] = False

# Print both to compare
print("Original: ", config.settings)
print("Snapshot: ", config_snapshot)