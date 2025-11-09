"""
Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(),
which prints each text message.
"""
def show_messages(messages):
   """Print all messages from the list."""
   for message in messages:
       print(message)

def send_messages(messages, sent_messages):
   """Send each message and move it to the sent_messages list."""
   while messages:
       current_message = messages.pop(0)
       print(f"Sending message: {current_message}")
       sent_messages.append(current_message)

# Original list of messages
text_messages = [
   "Hey, how are you?",
   "Don’t forget the meeting at 2 PM.",
   "Call me when you're free.",
   "Happy birthday!",
   "Let’s grab lunch tomorrow."
]

# Empty list to hold sent messages
sent_messages = []

# Call the function
send_messages(text_messages, sent_messages)

# Print both lists to verify
print("\nOriginal messages list:")
print(text_messages)

print("\nSent messages list:")
print(sent_messages)
