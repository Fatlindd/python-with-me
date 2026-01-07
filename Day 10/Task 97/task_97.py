"""
Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three
names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to
the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a
file is missing. Move one of the files to a diﬀerent location on your system, and make sure the code in the except
block executes properly.
"""
filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
   try:
       with open(file) as f:
           contents = f.read()
           print(f"\nContents of {file}:")
           print(contents)
   except FileNotFoundError:
       print(f"\nSorry, the file {file} was not found.")