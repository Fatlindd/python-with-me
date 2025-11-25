"""
Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and then
write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.
"""
# Start an infinite loop to collect guest names
print("Enter 'q' anytime to quit.\n")

while True:
    name = input("Please enter your name: ")

    if name.lower() == 'q':
        break

    # Append the name to guest_book.txt
    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")

    print(f"Hello {name}, your name has been added to the guest book.\n")