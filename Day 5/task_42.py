"""
Pets: Make several dictionaries, where each dictionary represents a diﬀerent pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
"""
# Pets

# Each dictionary represents a pet
pet_1 = {
   "animal": "dog",
   "owner": "Arta"
}

pet_2 = {
   "animal": "cat",
   "owner": "Besim"
}

pet_3 = {
   "animal": "parrot",
   "owner": "Dren"
}

pet_4 = {
   "animal": "hamster",
   "owner": "Elira"
}

pet_5 = {
   "animal": "rabbit",
   "owner": "Flamur"
}

# List of all pets
pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

# Loop through the list and print pet details
for index, pet in enumerate(pets, start=1):
   print(f"\nPet #{index}")
   print(f"Animal: {pet['animal'].title()}")
   print(f"Owner: {pet['owner'].title()}")