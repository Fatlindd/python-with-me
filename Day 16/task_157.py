"""
Round Off Prices in a Shopping Cart

You are required to:
Create a list of item prices in float format (e.g., [19.754, 4.989, 10.5, 2.335]).
Use the round() function to:
Round each price to 2 decimal places (simulate rounding to currency format).
Round each price to the nearest whole number (simulate invoice total preview).
Print both results clearly.
"""
def round_prices():
    prices = [19.754, 4.989, 10.5, 2.335]

    # Round to 2 decimal places
    rounded_to_two = [round(price, 2) for price in prices]
    print("Rounded to 2 decimal places: ", rounded_to_two)

    # Round to nearest whole number
    rounded_whole = [round(price) for price in rounded_to_two]
    print("Rounded to nearest whole number:", rounded_whole)

round_prices()

