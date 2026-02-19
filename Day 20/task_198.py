"""
Format and Analyze User Feedback for NLP Processing

Requirements
You’re part of a backend system that processes raw user feedback from a form submission. Your task is to:
1. Normalize each feedback message to ensure it's lowercase and consistently formatted.
2. Capitalize the first word of each message for readability.
3. Count how many times the word "bug" appears in the feedback (case-insensitive).
4. Ensure each feedback string is centered within a fixed width for alignment in logs.
5. Convert the text to a UTF-8 encoded format before storage.
6. Verify if the feedback ends with a period "." to ensure proper punctuation.
    feedbacks = [
       "  this App has a bug.  ",
       "Another bug found in checkout flow!",
       "i love this product",
       "BUG report: something is wrong",
       "the login page crashes."
]
"""
from openpyxl.styles.builtins import normal

feedbacks = [
   "  this App has a bug.  ",
   "Another bug found in checkout flow!",
   "i love this product",
   "BUG report: something is wrong",
   "the login page crashes."
]

BUG_COUNTER = 0
WIDTH = 50  # for centering logs

for raw_feedback in feedbacks:
    # 1. Trim and normalize to lowercase
    normalized = raw_feedback.strip().casefold()

    # 2. Capitalize for display
    display = normalized.capitalize()

    # 3. Count occurrences of "bug"
    BUG_COUNTER += normalized.count("bug")

    # 4. Center the output
    centered = display.center(WIDTH, "-")

    # 5. Encode the string
    encoded = centered.encode("utf-8")

    # 6. Check if ends with a period
    ends_properly = normalized.endswith(".")

    print("Centered:", centered)
    print("Encoded (UTF-8):", encoded)
    print("Ends with '.'?", ends_properly)
    print("===")

print("Total 'bug' mentions:", BUG_COUNTER)