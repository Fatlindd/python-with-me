"""
You are designing a plugin system that loads various components. Some components are functions (callables), while
others are just configuration objects or strings.

Create a program that:
Stores a mix of functions, strings, and integers in a list.
Uses the callable() function to filter only the callables.
Executes each callable safely and prints a result.
"""
# Example functions (plugins)
def greet():
    return "Hello, World!"

def get_sum():
    return 10 + 20

# Not a function
config = {'env': "production"}
name = "E-commerce plugin"
version = 2

# Plugin registry
components = [greet, config, name, get_sum, version]

# Iterate and filter only callable components
for idx, component in enumerate(components):
    if callable(component):
        result = component() # Safe to call
        print(f"component: {idx} is callable -> Output: {result}")
    else:
        print(f"Component: {idx} is NOT callable -> Value: {component}")
