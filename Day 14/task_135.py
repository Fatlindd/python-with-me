"""
Use help() to Explore Python's Built-in Functions and Your Own Code.
Write a simple class Rectangle with two methods: area() and perimeter().
Use help() to view documentation for:
A built-in Python function (len, for example).
The custom class Rectangle.
Add docstrings to your class and methods to make the help(Rectangle) output meaningful.
"""
# Custom class with docstrings
class Rectangle:
    """
       A class to represent a rectangle.

       Attributes:
       ----------
       width : float
           The width of the rectangle.
       height : float
           The height of the rectangle.
    """
    def __init__(self, width, height):
        """
            Constructs all the necessary attributes for the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
            Calculates the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

# Using help() on built-in and custom objects
help(len)
print("-----------")
help(Rectangle)
