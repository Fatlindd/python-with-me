"""
Input Validator for a Dynamic Text Analyzer

Requirements
As part of a data validation module for user-generated content (e.g. usernames, titles, numeric fields), create a
script that processes a list of strings and applies various built-in string validation methods:
1. Validate alphanumeric constraints (isalnum, isalpha, isdigit, isdecimal, isnumeric)
2. Check formatting (islower, isupper, istitle, isspace, isidentifier)
3. Verify printable character safety (isascii, isprintable)

You must:
    - Iterate over a list of input strings.
    - For each string, return a dictionary of validation results using the methods.
    - Identify and label any strings that are suitable to be used as valid Python variable names.
"""
def analyze_strings(strings):
    results = []

    for s in strings:
        analysis = {
            "original": s,
            "isalnum": s.isalnum(),
            "isalpha": s.isalpha(),
            "isascii": s.isascii(),
            "isdecimal": s.isdecimal(),
            "isdigit": s.isdigit(),
            "isidentifier": s.isidentifier(),
            "islower": s.islower(),
            "isnumeric": s.isnumeric(),
            "isprintable": s.isprintable(),
            "isspace": s.isspace(),
            "istitle": s.istitle(),
            "isupper": s.isupper(),
            "is_valid_variable": s.isidentifier() and not s.isnumeric(),
        }

        results.append(analysis)
    return results

# Sample test
sample_inputs = [
   "username123",  # alphanumeric
   "HELLO",        # uppercase
   "hello world",  # has space
   "1234",         # digits only
   "  ",           # whitespace
   "Naïve",        # Non-ASCII character
   "titleCase",    # valid identifier
   "def",          # keyword, but valid identifier
   "99balloons",   # starts with digit, invalid identifier
   "\u2603",       # Unicode snowman ☃
]

from pprint import pprint
pprint(analyze_strings(sample_inputs))