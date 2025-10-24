# Every Function


# List of countries to visit
countries = ["Japan", "Norway", "Brazil", "Canada", "Greece"]


# 1. Finding the length of the list
print(f"Number of countries in the list: {len(countries)}")


# 2. Printing the list in reverse order (temporarily, with slicing)
print("\nList in reverse order (temporary using slicing):")
print(countries[::-1])

# OR using reverse() to change in place
countries.reverse()
print("\nList after reverse() (in-place):")
print(countries)

# Revert back to original order using reverse again
countries.reverse()

# 3. Sorting the list temporarily with sorted()
print("\nList sorted alphabetically (temporary):")
print(sorted(countries))

# 4. Show that original list is unchanged
print("\nOriginal list after using sorted():")
print(countries)

# 5. Sorting the list permanently using sort()
countries.sort()
print("\nList after sort() (permanently sorted):")
print(countries)

# 6. Sorting the list in reverse-alphabetical order permanently
countries.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(countries)