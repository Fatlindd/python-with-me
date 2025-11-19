"""
Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about
Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote two
times: print the contents once by reading in the entire file, and once by storing the lines in a list and then looping
over each line.
"""

"""
Create learning_python.txt with contexts below:

In Python you can automate repetitive tasks.
In Python you can work with files easily.
In Python you can build web apps.
In Python you can analyze data.

"""
with open("learning_python.txt") as file:
    contents = file.read()
    print("Reading full content:\n")
    print(contents)

# Read file line by line into a list
with open("learning_python.txt") as file:
    lines = file.readlines()

print("\nReading line by line:\n")
for line in lines:
    print(line.strip())
