"""
City Names: Write a function called city_country() that takes in the name of a city and its country. The function should
return a string formatted like this:  "Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_country(city, country):
   """Return a formatted string like 'City, Country'."""
   return f"{city.title()}, {country.title()}"

# Calling the function with three city-country pairs
print(city_country("santiago", "chile"))
print(city_country("berlin", "germany"))
print(city_country("kyoto", "japan"))
