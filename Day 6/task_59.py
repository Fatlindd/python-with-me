"""
T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on
the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call
the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
def make_shirt(size, message):
   """Prints a summary of the shirt being made."""
   print(f"Creating a {size} shirt with the message: '{message}'")

# Call the function using **positional arguments**
make_shirt("Large", "Code. Sleep. Repeat.")

# Call the function using **keyword arguments**
make_shirt(message="Hello World!", size="Medium")
