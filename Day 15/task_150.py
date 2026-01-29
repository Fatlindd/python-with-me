"""
Fetch the Next Odd Number from a Generator Using next()
You're going to:
Write a generator that yields odd numbers from a given list.
Use the next() function to manually retrieve values from the generator one at a time.
Handle the situation when there are no more items to return using StopIteration or the default parameter.
"""
numbers = [2, 5, 8, 9, 12, 15]

# Generator expression to yield only odd numbers
odd_numbers = (num for num in numbers if num % 2 != 0)

# Fetch items using next()
print("Next odd number:", next(odd_numbers, "No more odd numbers found."))
print("Next odd number:", next(odd_numbers, "No more odd numbers found."))
print("Next odd number:", next(odd_numbers, "No more odd numbers found."))
print("Next odd number:", next(odd_numbers, "No more odd numbers found."))