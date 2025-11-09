"""
Archived Messages: Start with your work from Exercise 66. Call the function send_messages() with a copy of the list of
messages. After calling the function, print both of your lists to show that the original list has retained its messages.
"""
def send_messages(messages, sent_messages):
   """Simulate sending messages and archive them into a new list."""
   while messages:
       current_message = messages.pop(0)
       print(f"Sending message: {current_message}")
       sent_messages.append(current_message)

# Original list of text messages
original_messages = [
   "Don't forget the meeting at 2 PM.",
   "See you tomorrow!",
   "Happy Birthday!",
   "Let me know once you're home.",
   "This is the final reminder."
]

# Make a copy to preserve original list
messages_copy = original_messages[:]

# Empty list for sent messages
sent_messages = []

# Call the function with the copy
send_messages(messages_copy, sent_messages)

# Print lists to confirm results
print("\nOriginal messages list (should be unchanged):")
print(original_messages)

print("\nSent messages list (archived messages):")
print(sent_messages)