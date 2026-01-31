"""
Reverse User Input Without Slicing

You are required to:
Ask the user to input a sentence.
Use the built-in reversed() function (not slicing [::-1]) to reverse:
The characters in the sentence.
The order of words in the sentence.
Print both reversed outputs with labels.
Constraints:
Do not use slicing to reverse ([::-1] is not allowed).
Use reversed() built-in function for both cases.
"""
def reverse_sentence_content():
   sentence = input("Enter a sentence: ")

   # Reverse characters in the whole sentence
   reversed_chars = ''.join(reversed(sentence))
   print("Characters reversed:", reversed_chars)

   # Reverse word order
   words = sentence.split()
   reversed_words = ' '.join(reversed(words))
   print("Words reversed:", reversed_words)

reverse_sentence_content()