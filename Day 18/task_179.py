"""
Implement a Pagination Reversal System Using reverse()

Requirements
You are developing a debugging utility for a paginated API system that returns items in reverse chronological order.
For testing, you need to simulate this by reversing a list of dummy data (representing items fetched from an API).
1. Write a function reverse_items(items: list) -> list that:
    - Uses the reverse() method to reverse the list in place.
    - Returns the modified list.
2. Demonstrate the function with:
    - items = ['Page1', 'Page2', 'Page3', 'Page4']
    - Show that the original list is modified in-place by printing before and after.
"""
def reverse_items(list):
    print("Before reversal:", items)
    items.reverse()
    print("After reversal:", items)
    return items

# Example usage
items = ['Page1', 'Page2', 'Page3', 'Page4']
reversed_list = reverse_items(items)