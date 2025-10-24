# List of places to visit (not in alphabetical order)
places = ["Tokyo", "Reykjavik", "New York", "Cape Town", "Barcelona"]

# 1. Print original list
print("Original list: ")
print(places)

# 2. Print alphabetically sorted list (without changing the original)
print("\nAlphabetical order (temporary): ")
print(sorted(places))

# 3. Confirm original list is unchanged
print("\nList after sorted(): ")
print(places)

# 4. Print reverse-alphabetical order(temporary)
print("\nReverse alphabetical order (temporary): ")
print(sorted(places, reverse=True))

# 5. Confirm original list is still unchanged
print("\nList after sorted(reverse=True): ")
print(places)

# 6. Reverse the list in-place
places.reverse()
print("\nList after reverse():")
print(places)

# 7. Reverse again to restore original order
places.reverse()
print("\nList after second reverse():")
print(places)

# 8. Sort list permanently in alphabetical order
places.sort()
print("\nList after sort():")
print(places)

# 9. Sort list permanently in reverse-alphabetical order
places.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(places)