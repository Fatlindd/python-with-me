"""
Simpler Code: The program file_reader .py in this section uses a temporary variable, lines, to show how splitlines()
works. You can skip the temporary variable and loop directly over the list that splitlines() returns:
"""
for line in contents.splitlines():

"""
Remove the temporary variable from each of the programs in this section, to make them more concise.

Goal:
Refactor your file-reading programs by removing temporary variables (like lines) and using the .splitlines() method
directly inside a loop.
"""
with open('learning_python.txt') as file:
   contents = file.read()
   lines = contents.splitlines()
   for line in lines:
       print(line)

"Refactored Version (Simpler Code):"
with open('learning_python.txt') as file:
   for line in file.read().splitlines():
       print(line)
