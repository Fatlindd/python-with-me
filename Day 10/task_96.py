"""
Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a
mistake and enter text instead of a number.
"""
print("Addition Calculator")
print("Enter 'q' at any time to quit.\n")

while True:
   num1 = input("Enter first number: ")
   if num1.lower() == 'q':
       break

   num2 = input("Enter second number: ")
   if num2.lower() == 'q':
       break

   try:
       result = int(num1) + int(num2)
   except ValueError:
       print("Invalid input. Please enter numbers only.\n")
   else:
       print(f"The result is: {result}\n")
