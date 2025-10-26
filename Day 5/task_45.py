"""
Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""
# Cities
cities = {
   "tokyo": {
       "country": "japan",
       "population": "37 million",
       "fact": "Tokyo is the most populous metropolitan area in the world."
   },
   "paris": {
       "country": "france",
       "population": "11 million",
       "fact": "Paris is known as the City of Light and is home to the Eiffel Tower."
   },
   "new york": {
       "country": "usa",
       "population": "8.5 million",
       "fact": "New York is nicknamed 'The Big Apple' and is famous for Times Square."
   }
}

# Loop through the cities and print their information
for city, info in cities.items():
   print(f"\nCity: {city.title()}")
   print(f"  Country: {info['country'].title()}")
   print(f"  Population: {info['population']}")
   print(f"  Fact: {info['fact']}")
