"""
You are creating a Unicode Explorer Tool for developers.  This tool should:
Ask the user to enter a list of Unicode numbers (code points).
Convert each number to its corresponding character using chr().
Display the resulting string with proper formatting.

Example input:
[65, 66, 67, 8364]

Expected output:
ABC€
"""
def unicode_to_string(code_points):
    try:
        characters = [chr(code) for code in code_points]
        print(f"characters: {characters}")
        return ''.join(characters)
    except ValueError as e:
        return f"Error: {e} (Check if all values are valid Unicode points."

# Example usage
input_codes = [65, 66, 67, 8364]  # A, B, C, €
output = unicode_to_string(input_codes)
print("Decoded string:", output)
