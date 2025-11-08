"""
Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love
Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a diﬀerent message.
"""
def make_shirt(size="Large", message="I love Python"):
   """Prints a summary of the shirt being made with default values."""
   print(f"Creating a {size} shirt with the message: '{message}'")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size="Medium")

# Custom shirt with a different message
make_shirt(size="Small", message="Keep Calm and Code On")
