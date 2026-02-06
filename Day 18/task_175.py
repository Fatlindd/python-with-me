"""
Trace the First Occurrence of a User Action in a Log Sequence

Requirements
You’re analyzing a user interaction log represented as a list of action strings. You need to:
1. Define a simulated log (list of actions) from a session.
2. Write a function first_occurrence(log, action) that:
    - Uses list.index() to return the position of the first occurrence of a specified action.
    - Raises a custom error message if the action doesn’t exist in the log.
3. Demonstrate the function with:
    - An action that exists multiple times
    - An action that does not exist
"""
def first_occurrence(log, action):
    try:
        position = log.index(action)
        return f"'{action}' first occurred at position {position}."
    except ValueError:
        return f"Action '{action}' not found in log."

# Simulated session log
session_log = [
   "login", "browse", "click", "scroll", "click", "logout"
]

# Test Cases
print(first_occurrence(session_log, "click"))   # Exists multiple times
print(first_occurrence(session_log, "purchase"))  # Does not exist
