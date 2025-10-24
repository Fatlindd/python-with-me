# Initial guest list
guests = ["Elon Musk", "Nikola Tesla", "Ada Lovelace"]

# Let everyone know there's more space
print("Good news! We found a bigger dinner table and have room for more guests.\n")

# Add new guests
guests.insert(0, "Marie Curie")
guests.insert(len(guests) // 2, "Isaac Newton")
guests.append("Steve Jobs")

# Send updated invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner this Saturday at 7 PM.")