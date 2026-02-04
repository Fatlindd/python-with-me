"""
Combine Lists Using zip() to Create Structured Data

Requirements
1. You are given three separate lists:
    - product_names → list of product names
    - product_prices → list of product prices
    - product_quantities → list of quantities in stock
2. Use the zip() function to:
    -Combine these lists into a list of tuples where each tuple represents a product with (name, price, quantity).
    - Print each product in a human-readable format:
      Example: "Product: Apple, Price: $1.5, Quantity: 30"
3. Explain the behavior when the lists have different lengths.
"""
product_names = ['Apple', 'Banana', 'Orange']
product_prices = [1.5, 0.75, 1.2]
product_quantities = [30, 45, 25]

# Combine the lists using zip
products = zip(product_names, product_prices, product_quantities)

# Print each product
for name, price, quantity in products:
    print(f"Product: {name}, Price: ${price}, Quantity: {quantity}")
