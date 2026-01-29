"""
Find the Cheapest Product Using min()
You're given a list of dictionaries, where each dictionary represents a product with a name and a price. Your task is to:
Use the min() function to find the product with the lowest price.
Print the name and price of the cheapest product in a readable format.
"""
products = [
   {"name": "Mouse", "price": 25},
   {"name": "Keyboard", "price": 45},
   {"name": "Monitor", "price": 150},
   {"name": "USB Cable", "price": 5}
]

def get_cheapest_product(products):
    return min(products, key=lambda x: x["price"])

print(get_cheapest_product(products))