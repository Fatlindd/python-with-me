"""
Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.
"""
glossary = {
   "variable": "A named value used to store data.",
   "list": "An ordered collection of items, written in square brackets.",
   "dictionary": "A collection of key-value pairs.",
   "loop": "A way to repeat actions for every item in a collection.",
   "if statement": "A conditional block that runs code only if a condition is true.",
   "function": "A reusable block of code that performs a specific task.",
   "boolean": "A data type with only two possible values: True or False.",
   "tuple": "An immutable (unchangeable) ordered collection of items.",
   "elif": "Short for 'else if'; used in conditional statements.",
   "PEP 8": "Python's official style guide for writing clean and readable code."
}

# Loop through the glossary and print formatted output
for term, meaning in glossary.items():
   print(f"{term.title()}:\n  {meaning}\n")