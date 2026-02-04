"""
Inspect and Modify Object Attributes with vars()

Requirements
1. Create a simple Python class called Book with the following attributes:
    - title
    - author
    - year
2. Create an instance of the Book class.
3. Use vars() to:
    - Retrieve the __dict__ of the object.
    - Print all current attributes and their values.
4. Dynamically update the year attribute using vars() and print the updated dictionary.
"""
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Create an instance
my_book = Book("Python Mastery", "Jane Doe", 2022)

# Use vars() to access the __dict__ of the object
attributes = vars(my_book)
print("Initial attributes:")
print(attributes)

# Modify an attribute using vars()
vars(my_book)['year'] = 2025
print("\nUpdated attributes:")
print(vars(my_book))
print(locals())
