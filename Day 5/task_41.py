"""
People: Make two new dictionaries representing diﬀerent people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
"""
# People

# Three dictionaries representing different people
person_1 = {
    "first_name": "Arta",
    "last_name": "Bajrami",
    "age": 28,
    "city": "Prishtina"
}

person_2 = {
    "first_name": "Dren",
    "last_name": "Gashi",
    "age": 32,
    "city": "Peja"
}

person_3 = {
    "first_name": "Dan",
    "last_name": "Garci",
    "age": 25,
    "city": "Gjilan"
}

# List of all people
people = [person_1, person_2, person_3]

# Loop through the list and print information about each person
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']

    print(f"\nName: {full_name}")
    print(f"Age: {age}")
    print(f"City: {city}")