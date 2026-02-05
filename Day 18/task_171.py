"""
Resetting a Shopping Cart with clear()

Requirements
You are building a mock shopping cart system. Your task is to:
1. Create a list called cart that holds some sample items ("Apple", "Bread", "Milk").
2. Print the cart contents.
3. Ask the user if they want to clear their cart using the input() function (yes or no).
4. If the user says yes, use the clear() method to empty the cart.
5. Print the cart contents again to show it is now empty.
"""
cart = ["Apple", "Bread", "Milk"]
print("Your shopping cart contains:", cart)

choice = input("Do you want to clear your cart (yes/no): ").strip().lower()

if choice == "yes":
    cart.clear()
    print("Cart has been cleared.")
else:
    print("Car was not been cleared.")

print("Current cart contents:", cart)