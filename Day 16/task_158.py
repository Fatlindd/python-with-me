"""
Clean Up a List of Duplicate Emails Using set()

You are required to:
Create a list of email addresses that may contain duplicates.
Use the set() function to:
Remove all duplicate emails.
Display a list of unique email addresses.
Convert the resulting set back into a sorted list and print it.
"""
def remove_duplicate_emails():
    emails = [
        "john@example.com", "jane@example.com", "john@example.com",
        "mike@example.com", "jane@example.com", "lisa@example.com"
    ]

    # Use set() to remove duplicates
    unique_emails = set(emails)
    print("Unique emails (as set):", unique_emails)

    # Convert to sorted list for display
    sorted_emails = sorted(list(unique_emails))
    print("Sorted unique emails (as list):", sorted_emails)

remove_duplicate_emails()