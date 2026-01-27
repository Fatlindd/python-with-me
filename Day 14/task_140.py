"""
Validate User Input Types with isinstance()
Write a function called process_payment that:
Accepts two parameters: amount and is_member.
Checks if:
amount is an integer or float.
is_member is a boolean.
If types are valid:
Apply a 10% discount to amount if is_member is True.
Return the final amount.
If types are invalid:
Raise a TypeError with a clear message.
Use isinstance() to implement all type checks.
"""
def process_payment(amount, is_member):
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be an integer or float.")

    if not isinstance(is_member, bool):
        raise TypeError("is_member must be a boolean (True or False).")

    if is_member:
        amount *= 0.9 # Apply 10% discount

    return round(amount, 2)

try:
    print(process_payment(100, True))
    print(process_payment(250.5, False))
    print(process_payment("free", True))
except TypeError as e:
    print(f"Error: {e}")