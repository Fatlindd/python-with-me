"""
Dynamically Create and Access Global Variables Using globals()
Write a Python function that accepts a key (variable name) and a value.
Use globals() to dynamically create a global variable using the given key.
Access and print the value of this global variable afterward using globals().
"""
def create_global_var(var_name, value):
    globals()[var_name] = value

# Create a global variable named 'project_name'
create_global_var("project_name", "Dashboard")

# Access and print it using globals()
print("Project Name: ", globals()["project_name"])

# Now you can use it like a normal global variable
print("Access without globals():", project_name)
