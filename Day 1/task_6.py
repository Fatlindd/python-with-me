# Guest list from Exercise 3-6
guests = ["Marie Curie", "Elon Musk", "Isaac Newton", "Nikola Tesla", "Ada Lovelace", "Steve Jobs"]

# Let everyone know about the change in plan
print("Unfortunately, the new dinner table won't arrive in time.")
print("We can only invite two people to dinner.\n")

# Remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, we can't invite you to dinner this time.")


# Inform the two remaining guests
print()
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner this Saturday at 7 PM!")

# Empty the list completely
del guests[0]
del guests[0]

# Confirm the list is empty
print("\nFinal guest list: ", guests)