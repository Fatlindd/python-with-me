"""
Use sorted() to Organize and Manipulate Data

Requirements
1. Create a list of dictionaries representing people with name and age keys.
2. Use the sorted() function to:
   - Sort the list of people by age (ascending).
   - Sort the list by name (alphabetically).
   - Sort the list by age in descending order.
3. Print the results of each sorting operation.
"""
people = [
   {'name': 'Alice', 'age': 30},
   {'name': 'Bob', 'age': 25},
   {'name': 'Charlie', 'age': 35},
   {'name': 'David', 'age': 28}
]

# Sort by age (ascending)
by_age = sorted(people, key=lambda person: person['age'])

# Sort by name (alphabetically)
by_name = sorted(people, key=lambda person: person['name'])

# Sort by age (descending)
by_age_desc = sorted(people, key=lambda person: person['age'], reverse=True)

# Output
print("Sorted by age (asc):", by_age)
print("Sorted by name:", by_name)
print("Sorted by age (desc):", by_age_desc)