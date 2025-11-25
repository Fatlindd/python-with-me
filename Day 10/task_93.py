"""
Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called
guest.txt.
"""
# Prompt the user for their name
name = input("What is your name? ")

# Open the file in write mode and save the name
with open("guest.txt", "w") as file:
   file.write(name)