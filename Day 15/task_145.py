"""
Inspect Local Variables in a Function for Debugging
Write a function that calculates basic employee data like name, age, and salary.
Inside the function, use the locals() function to retrieve and display all local variables.
This is useful for debugging, logging, or dynamically inspecting the function's internal state.
"""
def employee_summary():
    name = "John Doe"
    age = 30
    salary = 55000

    # Print all local variables inside the function
    local_vars = locals()
    print("Local variables inside employee_summary(): ")
    for key, value in local_vars.items():
        print(f"{key}: {value}")

# Call the function
employee_summary()