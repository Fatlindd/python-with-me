"""
Convert Decimal RGB Color to Hex Code Using hex()
Create a function rgb_to_hex(r, g, b) that:
Accepts three integers (r, g, b) in the range 0–255 representing Red, Green, and Blue.
Converts each of them into a 2-digit hexadecimal string.
Returns a string representing the full hex color code (e.g., #FF0000 for red).

Use the hex() function to perform the conversion.
Validate that the function works for common colors like red, green, blue, and white.
"""
def rgb_to_hex(r, g, b):
    # Ensure RGB values are within 0–255
    if not all(0 <= val <= 255 for val in (r, g, b)):
        raise ValueError("Each color component must be in the range 0-255.")

    # Convert each component to hex and remove the '0x' prefix
    # Then pad with 0 if single digit and uppercase it
    red_hex = hex(r)[2:].zfill(2).upper()
    green_hex = hex(g)[2:].zfill(2).upper()
    blue_hex = hex(b)[2:].zfill(2).upper()

    return f"#{red_hex}{green_hex}{blue_hex}"

# Example usage
print(rgb_to_hex(255, 0, 0))    # Output: #FF0000 (Red)
