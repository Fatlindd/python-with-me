"""
Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers.
When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers.
Add them together and print the result. Catch the ValueError if either input value is not a number, and print a
friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.
"""
print("Give me two numbers to add.")
print("Enter 'q' to quit.\n")

while True:
    num1 = input("First number: ")
    if num1.lower() == 'q':
        break

    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break

    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Opps! Please enter valid numbers only. \n")
    else:
        print(f"The result is: {result} \n")