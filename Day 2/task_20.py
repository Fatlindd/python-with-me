# Slices
# Reuse the cube list from 1 to 10
cubes = [number ** 3 for number in range(1, 11)]

# Print the entire list (optional, just to see it)
print("Full list of cubes:", cubes)

# First 3 items
print("\nThe first three items in the list are:")
print(cubes[:3])  # indexes 0, 1, 2

# Middle 3 items
print("\nThree items from the middle of the list are:")
print(cubes[3:6])  # indexes 3, 4, 5 (could vary — this is one option)

# Last 3 items
print("\nThe last three items in the list are:")
print(cubes[-3:])  # indexes 7, 8, 9

print(cubes[::2])