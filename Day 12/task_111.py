"""
You're building a developer debugging tool that:
Accepts a list of decimal numbers representing user permission flags (e.g., 4 = Read, 2 = Write, 1 = Execute).
Converts each permission into its binary representation using bin().
Displays a formatted table comparing decimal and binary permissions.
Help developers quickly understand permission bit flags using binary conversion.
"""
def display_permission_flags(codes):
    print(f"{'Decimal': <10} {'Binary': <10}")
    print("-" * 22)
    for code in codes:
        binary  = bin(code)
        print(f"{code:<10} {binary:<10}")

permission_codes = [7, 5, 3, 2, 1, 0]
display_permission_flags(permission_codes)