"""
Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
"""

# Extended Cities Program – With More Info & Better Formatting
cities = {
   "tokyo": {
       "country": "japan",
       "population": "37 million",
       "fact": "Most populous metro area in the world.",
       "language": "Japanese",
       "currency": "Yen"
   },
   "paris": {
       "country": "france",
       "population": "11 million",
       "fact": "Home to the Eiffel Tower and the Louvre.",
       "language": "French",
       "currency": "Euro"
   },
   "new york": {
       "country": "usa",
       "population": "8.5 million",
       "fact": "Known as 'The Big Apple' and never sleeps.",
       "language": "English",
       "currency": "US Dollar"
   }
}

# Loop through cities and print all information in a nicely formatted way
for city, info in cities.items():
   print("=" * 40)
   print(f"🌆 City: {city.title()}")
   print(f"🌍 Country: {info['country'].title()}")
   print(f"👥 Population: {info['population']}")
   print(f"🗣️ Language: {info['language']}")
   print(f"💰 Currency: {info['currency']}")
   print(f"📌 Fun Fact: {info['fact']}")
   print("=" * 40 + "\n")
