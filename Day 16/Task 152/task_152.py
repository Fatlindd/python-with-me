"""
Read, Modify, and Save a File Using open()
You will:
Create a text file named sample.txt with the following lines:
Python is fun.
Let's learn more.
Built-in functions are powerful.
Read the contents of the file using the open() function in read mode ('r').
Convert all text to uppercase.
Write the modified text into a new file named output.txt using write mode ('w').
Use context managers (with statement) to ensure proper file handling.
"""
# Step 1: Create sample.txt manually or with this code once
with open('sample.txt', 'w') as f:
   f.write("Python is fun.\nLet's learn more.\nBuilt-in functions are powerful.\n")

# Step 2: Read and transform content
with open('sample.txt', 'r') as infile:
   content = infile.read()

# Step 3: Modify content to uppercase
modified_content = content.upper()

# Step 4: Write to a new file
with open('output.txt', 'w') as outfile:
   outfile.write(modified_content)

print("✅ File processed. Check 'output.txt'")