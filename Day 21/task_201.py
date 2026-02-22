"""
Create a Text Processing Utility

Requirements
Create a TextFormatter class that receives a list of user input strings and performs a series of formatting and
transformation operations:
1. Trim and lowercase all strings.
2. Left-justify each cleaned string to a fixed width for aligned output.
3. Join all strings into a single string using a delimiter.
4. Use partition() to split the joined string at a target keyword into 3 parts.
5. Use replace() to replace a specific word with another.
6. Use maketrans() to create a character substitution map (e.g., replace vowels with *).
7. Return both intermediate and final results for inspection.
"""
class TextFormatter:
    def __init__(self, texts, width=20, delimiter=" | "):
        self.original = texts
        self.width = width
        self.delimiter = delimiter

    def process(self, keyword, to_replace, replacement):
        # Step 1: Clean and lowercase
        cleaned = [txt.lstrip().lower() for txt in self.original]

        # Step 2: Left-justify each string
        justified = [txt.ljust(self.width) for txt in cleaned]

        # Step 3: Join into one string
        joined = self.delimiter.join(justified)

        # Step 4: Partition at keyword
        before, match, after = joined.partition(replacement)

        # Step 5: Replace a word
        replaced = joined.replace(to_replace, replacement)

        # Step 6: Translate vowels to *
        trans_table = str.maketrans("aeiou", "*****")
        translated = replaced.translate(trans_table)

        return {
            "cleaned": cleaned,
            "justified": justified,
            "joined": joined,
            "partition": (before, match, after),
            "replaced": replaced,
            "translated": translated,
        }

# Test
texts = ["   Banana", "Apple", " Pear", "Grape"]
formatter = TextFormatter(texts)
results = formatter.process(keyword="pear", to_replace="apple", replacement="mango")

from pprint import pprint
pprint(results)