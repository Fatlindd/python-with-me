"""
Movie Tickets: A movie theater charges diﬀerent ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
"""
# Movie Tickets
print("Enter 'quit' to stop.")
while True:
   age_input = input("How old are you? ")
   if age_input.lower() == 'quit':
       print("Thanks for checking our ticket prices!")
       break

   age = int(age_input)
   if age < 3:
       print("Your ticket is free!")
   elif age <= 12:
       print("Your ticket costs $10.")
   else:
       print("Your ticket costs $15.")