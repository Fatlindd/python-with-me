"""
Using hash() to Uniquely Identify Objects in a Set
Create a class Product with attributes: name and price.
Implement the __hash__() and __eq__() methods so that two Product objects with the same name and price are treated as
the same in sets.
Store multiple Product objects in a set and show that duplicates (same name and price) are not added twice.
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

# Create products
p1 = Product("Laptop", 2000)
p2 = Product("Laptop", 2000)
p3 = Product("Phone", 800)

# Use set to eliminate duplicates
product_set = {p1, p2, p3}

print(product_set)