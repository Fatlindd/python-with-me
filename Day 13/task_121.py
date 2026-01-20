"""
You are building a simple inventory system for an online store.
Use the dict() constructor to create a dictionary of products.
Each product should have a name, price, and quantity.
Display the product information in a readable format.
Add a new product to the inventory using dict() syntax.
"""
inventory = {
   "laptop": dict(name="Laptop", price=999.99, quantity=10),
   "mouse": dict(name="Wireless Mouse", price=25.50, quantity=50),
   "keyboard": dict(name="Mechanical Keyboard", price=70.00, quantity=30)
}

# Display inventory
for product_key, product_info in inventory.items():
    print(f"{product_key.title()} Info: ")
    for key, value in product_info.items():
        print(f"{key.title()}: {value}")
    print()

# Add a new product using dict() with list of tuples
inventory['monitor'] = dict([("name", "24 inch Monitor"), ("price", 149.99), ("quantity", 20)])

# Confirm new product added
print("After adding Monitor: ")
for k, v in inventory["monitor"].items():
    print(f"{k.title()}: {v}")