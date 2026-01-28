"""
Convert User Input to a List of Words
Write a program that asks the user to input a comma-separated string of items (e.g., "apple,banana,grape").
Convert the user input into a list of strings.
Use the list() function intentionally, so the developer can see when it's appropriate and when it's not.
Print the final list to the user.
"""
# Step 1: Get comma-separated input
user_input = input("Enter items separated by commas: ")

# Step 2: Split the input string into words
word_list = user_input.split(",")

# Step 3: Optional - use list() to convert to list explicitly (even though split returns a list)
final_list = list(word_list)

# Step 4: Output result
print(f"Here's your list: {final_list}")