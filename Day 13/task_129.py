"""
Invoice Generator Using format()
Create a small script that generates an invoice summary.
Prompt the user for a product name, quantity, and unit price.
Calculate the total and format the output neatly using format().
Display the final output as a formatted string like this:
"""
# Collect data
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

# Calculate total
total = quantity * unit_price

# Display form atted result using format()
output = (
   "Product: {}\n"
   "Quantity: {}\n"
   "Unit Price: ${:.2f}\n"
   "Total: ${:.2f}"
).format(product, quantity, unit_price, total)

print("\n--- Invoice Summary ---")
print(output)