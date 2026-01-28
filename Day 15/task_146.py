"""
Convert a List of Prices from USD to EUR
You have a list of product prices in USD.
Write a function that converts a single price from USD to EUR (assume 1 USD = 0.85 EUR).
Use the map() function to apply this conversion to all prices in the list.
Print the converted prices.
"""
# Step 1: Conversion function
def usd_to_eur(price_usd):
    return round(price_usd * 0.85, 2)

# Step 2: List of prices in USD
prices_usd = [10, 20, 50.5, 100, 250.75]

# Step 3: Convert using map
prices_eur = list(map(usd_to_eur, prices_usd))

# Step 4: Display the results
print("Prices in EUR: ", prices_eur)