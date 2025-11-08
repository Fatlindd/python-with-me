"""
Three Exits: Write diﬀerent versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit' value.
"""

# Version 1: Using a conditional test in the while statement
age_input = ""
while age_input.lower() != 'quit':
   age_input = input("How old are you? (Type 'quit' to exit): ")

   if age_input.lower() != 'quit':
       age = int(age_input)
       if age < 3:
           print("Your ticket is free!")
       elif age <= 12:
           print("Your ticket costs $10.")
       else:
           print("Your ticket costs $15.")

# Version 2: Using an active variable
active = True
while active:
   age_input = input("How old are you? (Type 'quit' to exit): ")

   if age_input.lower() == 'quit':
       active = False
   else:
       age = int(age_input)
       if age < 3:
           print("Your ticket is free!")
       elif age <= 12:
           print("Your ticket costs $10.")
       else:
           print("Your ticket costs $15.")

# Version 3: Using a break statement
while True:
   age_input = input("How old are you? (Type 'quit' to exit): ")

   if age_input.lower() == 'quit':
       break

   age = int(age_input)
   if age < 3:
       print("Your ticket is free!")
   elif age <= 12:
       print("Your ticket costs $10.")
   else:
       print("Your ticket costs $15.")
