# One Million

# Create a range from 1 to 1,000,000 (inclusive)
numbers = range(1, 100)

# for number in numbers:
#     print(number)

for number in list(numbers)[:5]:
    print(number)

for number in list(numbers)[-5:]:
    print(number)