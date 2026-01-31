"""
Logging Objects Using repr()
You are asked to build a simple logging system that logs operations performed on products. Each log entry should
include a readable representation of the product object using the repr() built-in function.

Your task is to:
Create a Product class with attributes: name, price, and quantity.
Implement a __repr__() method in the class to return a detailed string representation.
Write a function log_action(product, action) that:
Accepts a product object and a string describing the action.
Returns a log string like:
 "LOG: <action> was performed on Product(name='Laptop', price=1000.0, quantity=5)"
 using repr(product).
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

def log_action(product, action):
    return f"LOG: {action} was performed on {repr(product)}"

# Example usage
p1 = Product("Laptop", 1000.0, 5)
print(log_action(p1, "Update"))