# Initial guest list
guests = ["Elon Musk", "Albert Einstein", "Ada Lovelace"]


# Print the original invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner this Saturday at 7 PM.")

# One guest can't make it
unavailable_guest = 'Albert Einstein'
print(f"\nUnfortunately, {unavailable_guest} can't make it to the dinner.")

# Replace the unavailable guest with a new one
replacement_guest = "Nikola Tesla"
index = guests.index(unavailable_guest)
guests[index] = replacement_guest

# Print new invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner this Saturday at 7 PM.")