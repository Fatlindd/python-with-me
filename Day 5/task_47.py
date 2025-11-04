"""
Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
"""

# Rental Car
# Ask the user what kind of rental car they would like
car = input("What kind of rental car would you like? ")

# Print a personalized message
print(f"Let me see if I can find you a {car.title()}.")
