"""
Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should
print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call
your function for three diﬀerent cities, at least one of which is not in the default country.
"""

def describe_city(city, country="Iceland"):
   """Prints a sentence stating which country a city is in, with a default country."""
   print(f"{city.title()} is in {country.title()}.")

# Function calls
describe_city("reykjavik")             # Uses default country (Iceland)
describe_city("akureyri")              # Uses default country (Iceland)
describe_city("tokyo", "japan")        # Overrides default with a new country
