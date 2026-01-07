"""
Silent Cats and Dogs: Modify your except block in Exercise 97 to fail silently if either file is missing.
"""
filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
   try:
       with open(file) as f:
           contents = f.read()
           print(f"\nContents of {file}:")
           print(contents)
   except FileNotFoundError:
       pass  # Silently skip missing files
