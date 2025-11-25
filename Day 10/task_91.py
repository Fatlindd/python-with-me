"""
Learning C: You can use the replace() method to replace any word in a string with a diﬀerent word. Here’s a quick
example showing how to replace 'dog' with 'cat' in a sentence:

Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of
another language, such as C. Print each modified line to the screen.
"""
# Open and read the file line by line
with open('learning_python.txt') as file:
   for line in file:
       # Replace 'Python' with 'C' and print
       modified_line = line.replace('Python', 'C')
       print(modified_line.strip())
