"""
 More Conditional Tests: You don’t have to limit the number of tests you create to 10. Have at least one True and one False result for each of the following:
Tests for equality and inequality with strings
Tests using the lower() method
Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
Tests using the and keyword and the or keyword
Test whether an item is in a list
Test whether an item is not in a list
"""

# Equality and inequality with strings
fruit = 'Apple'
print("Is fruit == 'Apple'? I predict True.")
print(fruit == 'Apple')

print("\nIs fruit != 'Banana'? I predict True.")
print(fruit != 'Banana')

print("\nIs fruit == 'apple'? I predict False.")
print(fruit == 'apple')

# Using lower()
print("\nIs fruit.lower() == 'apple'? I predict True.")
print(fruit.lower() == 'apple')

print("\nIs fruit.lower() == 'banana'? I predict False.")
print(fruit.lower() == 'banana')

# Numerical tests
age = 20
print("\nIs age == 20? I predict True.")
print(age == 20)  # True


print("\nIs age != 18? I predict True.")
print(age != 18)  # True


print("\nIs age > 18? I predict True.")
print(age > 18)  # True


print("\nIs age < 30? I predict True.")
print(age < 30)  # True


print("\nIs age >= 21? I predict False.")
print(age >= 21)  # False


print("\nIs age <= 20? I predict True.")
print(age <= 20)  # True


# Using and/or
score = 85
print("\nIs score > 80 and score < 90? I predict True.")
print(score > 80 and score < 90)  # True


print("\nIs score > 90 or score == 85? I predict True.")
print(score > 90 or score == 85)  # True


print("\nIs score < 80 and score > 70? I predict False.")
print(score < 80 and score > 70)  # False


# Membership tests
colors = ['red', 'green', 'blue']


print("\nIs 'green' in colors? I predict True.")
print('green' in colors)  # True


print("\nIs 'yellow' in colors? I predict False.")
print('yellow' in colors)  # False


print("\nIs 'purple' not in colors? I predict True.")
print('purple' not in colors)  # True


print("\nIs 'red' not in colors? I predict False.")
print('red' not in colors)  # False
