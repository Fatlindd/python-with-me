"""
Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(),
which prints each text message.
"""
def show_messages(messages):
   """Print each message in the list."""
   for message in messages:
       print(message)

# List of text messages
text_messages = [
   "Hey, how are you?",
   "Don’t forget the meeting at 2 PM.",
   "Call me when you're free.",
   "Happy birthday!",
   "Let’s grab lunch tomorrow."
]

# Calling the function
show_messages(text_messages)
