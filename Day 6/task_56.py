"""
Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could
visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
"""
# Dictionary to store responses
dream_vacations = {}

# Polling active flag
polling_active = True
while polling_active:
   # Ask for name and dream vacation
   name = input("\nWhat is your name? ")
   place = input("If you could visit one place in the world, where would you go? ")

   # Store the response
   dream_vacations[name] = place

   # Ask if someone else wants to respond
   repeat = input("Would you like to let another person respond? (yes/no) ")
   if repeat.lower() != 'yes':
       polling_active = False

# Print poll results
print("\n--- Dream Vacation Poll Results ---")
for name, place in dream_vacations.items():
   print(f"{name.title()} would like to visit {place.title()}.")
