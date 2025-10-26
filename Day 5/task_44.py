"""
Favorite Numbers: Each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
"""
# Favorite Numbers (multiple per person)
favorite_numbers = {
   "Arta": [7, 13],
   "Besim": [11],
   "Dren": [3, 5, 9],
   "Elira": [9, 21],
   "Flamur": [5]
}

# Loop through the dictionary
for name, numbers in favorite_numbers.items():
   print(f"\n{name}'s favorite number(s):")
   for number in numbers:
       print(f"- {number}")
