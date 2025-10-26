"""
Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as a neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
glossary = {
   "variable": "A named value used to store data.",
   "list": "An ordered collection of items, written in square brackets.",
   "dictionary": "A collection of key-value pairs.",
   "loop": "A way to repeat actions for every item in a collection.",
   "if statement": "A conditional block that runs code only if a condition is true."
}

# Print each word and its definition
for word, definition in glossary.items():
   print(f"{word.title()}:\n  {definition}\n")