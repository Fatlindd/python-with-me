"""
Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.
"""
# Favorite Places

favorite_places = {
   "Arta": ["Paris", "Rome", "New York"],
   "Dren": ["Tokyo", "Kyoto"],
   "Elira": ["Barcelona"]
}

# Loop through the dictionary and print favorite places for each person
for name, places in favorite_places.items():
   print(f"\n{name}'s favorite place(s):")
   for place in places:
       print(f"- {place}")
