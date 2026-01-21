"""
1. Write a program that calculates the number of 1 Euro coins and remaining cents when a user enters an amount in cents.
2. Use the divmod() built-in function to efficiently compute both:
   - How many 100-cent (1 Euro) coins can be given
   - What’s left over as remaining cents
"""
def coin_change(amount_in_cents):
    euros, cents = divmod(amount_in_cents, 100)
    print(f"You will get {euros} Euro coin(s) and {cents} cent(s).")

# Example usage
amount = int(input("Enter an amount in cents: "))
coin_change(amount)