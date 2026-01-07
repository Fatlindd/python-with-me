"""
Common Words: Visit Project Gutenberg (https://gutenberg.org) and find a few texts you’d like to analyze. Download the
text files for these works, or copy the raw text from your browser into a text file on your computer.

You can use the count() method to find out how many times a word or phrase appears in a string. For example, the
following code counts the number of times 'row' appears in a string:
"""
line = "Row, row, row your boat"
print(line.count('row'))
print(line.lower().count('row'))

def count_word_occurrences(filename, word):
   try:
       with open(filename, encoding='utf-8') as f:
           contents = f.read().lower()
   except FileNotFoundError:
       print(f"Sorry, the file {filename} was not found.")
   else:
       word_count = contents.count(word)
       print(f"The word '{word}' appears about {word_count} times in {filename}.")

# Example usage
count_word_occurrences('alice_in_wonderland.txt', 'the')      # may include 'then', 'there'
count_word_occurrences('alice_in_wonderland.txt', 'the ')     # more accurate
