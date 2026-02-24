"""
Multi-Stage String Sanitizer and Formatter for User Records

Requirements
You're tasked with building a function that takes a multi-line raw user database dump and transforms it into a clean,
structured, and secure report using the built-in string methods above.

Each line may contain a record in the format:
name: alice wonderland, email: alice@domain.com, id: 42

Your job is to:
1. Split the raw dump into lines → splitlines()
2. For each line:
    - Remove leading/trailing whitespace → strip()
    - Ensure it starts with 'name:' → startswith()
    - Convert name to title case → title()
    - Convert email to uppercase → upper()
    - Swap case in notes field (if any) → swapcase()
    - Pad ID to 6 digits using → zfill()
    - Remove sensitive keywords (like "password") using → translate() with a custom mapping
    - Finally, use → split() to parse name, email, id as keys
"""
def sanitize_user_dump(raw_data: str) -> str:
    lines = raw_data.splitlines()
    cleaned_records = []

    # Custom translation map to sanitize keywords
    table = str.maketrans({'p': '*', 'a': '*'})  # Example: 'password' → '*ssword'

    for line in lines:
        line = line.strip()

        if not line.startswith("name:"):
            continue

        parts = line.split(",")
        record = {}

        for part in parts:
            print(f"part: {part}")
            key, value = part.strip().split(":", 1)
            print(f"key: {key}, value: {value}")
            key = key.strip().lower()
            value = value.strip()

            if key == "name":
                record["name"] = value.title()
            elif key == "email":
                record["email"] = value.upper()
            elif key == "id":
                record["id"] = value.zfill(6)
            elif key == "note":
                record["note"] = value.swapcase().translate(table)

        cleaned_records.append(record)

    return cleaned_records

# Example usage
raw_dump = """
 name: alice wonderland, email: alice@domain.com, id: 42
 name: BOB smith, email: bob@example.org, id: 7, note: this is a Password Hint
 name:   charlie Brown  , email:  charlie@brown.io , id: 123
"""

from pprint import pprint
pprint(sanitize_user_dump(raw_dump))
