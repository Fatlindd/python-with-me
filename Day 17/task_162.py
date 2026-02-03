"""
Use staticmethod() to Create Utility Logic Inside a Class

Requirements
1. Create a MathUtils class.
2. Inside the class, define a method is_even(number) that checks if a number is even.
3. Convert this method into a static method using staticmethod().
4. Show how to call the method directly from the class without creating an instance.
5. Print the result for multiple numbers to demonstrate usage.
"""
class MathUtils:
    def is_even(number):
        return number % 2 == 0

    # Convert to static method
    is_even = staticmethod(is_even)

# Use static method without creating an instance
print(MathUtils.is_even(10))
print(MathUtils.is_even(7))