"""
Create a custom class called Book with a couple of attributes and methods.
Instantiate the class and use dir() to explore:
The default attributes and methods of the instance.
The differences between using dir() on the class and on an instance.
Also use dir() on a built-in object like a string to compare the output.
"""
# Define a simple Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        return f"Reading {self.title} by {self.author}"

    def summary(self):
        return f"{self.title} is a great book."

# Create an instance of the Book class
my_book = Book("Atomic Habits", "James Clear")

# Use dir() on the instance
print("Attributes and methods of my_book:")
print(dir(my_book))
print("\n")

# Use dir() on the class
print("Attributes and methods of Book class:")
print(dir(Book))
print("\n")

# Use dir() on a string object
sample_string = "hello"
print("Attributes and methods of a string object:")
print(dir(sample_string))


