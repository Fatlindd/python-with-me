"""
Calculate the Total Sales from a List of Daily Transactions

Requirements
1. You are given a list of daily sales transactions represented as floats:
 transactions = [245.50, 130.00, 99.99, 300.10, 150.25]
2. Use the built-in sum() function to calculate the total revenue.
3. Add logic to ignore negative values (if any).
4. Display the result with a descriptive message.
"""
transactions = [245.50, 130.00, 99.99, 300.10, 150.25]

# Filter out negative transactions (e.g., refunds)
valid_transactions = [t for t in transactions if t > 0]

# Calculate total revenue
total_sales = sum(valid_transactions)

# Display result
print(f"Total sales ammount is: ${total_sales:.2f}")
