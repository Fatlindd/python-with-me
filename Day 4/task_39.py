"""
Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'. Use a loop to print a sentence about each river, such as The Nile runs through Egypt .
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.
"""
rivers = {
   "nile": "egypt",
   "amazon": "brazil",
   "danube": "germany"
}

# 1. Print sentence about each river
for river, country in rivers.items():
   print(f"The {river.title()} runs through {country.title()}.")

# 2. Print the name of each river
print("\nRivers included in the dictionary:")
for river in rivers.keys():
   print(f"- {river.title()}")

# 3. Print the name of each country
print("\nCountries included in the dictionary:")
for country in rivers.values():
   print(f"- {country.title()}")
