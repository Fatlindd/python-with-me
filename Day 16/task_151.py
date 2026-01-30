"""
Use object() as a Sentinel Value in a Function

You will:
Create a function that filters out a target value from a list.
Use object() to define a unique sentinel default value in the function parameters.
Understand how object() ensures uniqueness and avoids conflict with any real user input.
"""
# Sentinel value created using object()
_sentinel = object()

def filter_out(data, target=_sentinel):
    print(target is _sentinel)
    if target is _sentinel:
        print("No target specified. Returning original list.")
        return data
    return [item for item in data if item != target]

# Usage examples
print(filter_out([1, 2, 3, 4, 2, 5], 2))
print(filter_out([1, 2, 3]))
print(filter_out([1, 2, 3], target=None))