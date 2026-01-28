"""
Custom Iterator for Processing Orders One by One
Create a list of orders: ["Order #1", "Order #2", "Order #3"]
Use the built-in iter() function to turn this list into an iterator.
Process each order manually using the next() function.
Handle the StopIteration exception gracefully after all orders are processed.
"""
# List of orders
orders = ["Order #1", "Order #2", "Order #3"]

# Convert list to iterator
order_iterator = iter(orders)

# Process orders one by one
while True:
    try:
        order = next(order_iterator)
        print(f"Processing {order}")
    except StopIteration:
        print("All orders have been processed.")
        break