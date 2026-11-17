# Supermarket Bill Generator Mini Project
# Dictionary to store available items and their prices (in ₹)
store_menu = {
    "apple": 50,
    "banana": 20,
    "milk": 30,
    "bread": 40,
    "eggs": 60,
    "coffee": 100
}
cart = []
total_amount = 0
print("Welcome to Python SuperMart!")
print("-" * 30)
print("Available Items:")
for item, price in store_menu.items():
    print(f"{item.capitalize()}: ₹{price}")
print("-" * 30)
# Loop to take customer orders
while True:
    choice = input("\nEnter item to buy (or type 'done' to checkout): ").strip().lower()

    if choice == 'done':
        break

    if choice in store_menu:
        try:
            quantity = int(input(f"Enter quantity for {choice}: "))
            if quantity > 0:
                item_total_price = store_menu[choice] * quantity
                # Add item details to the cart list
                cart.append((choice, quantity, item_total_price))
                total_amount += item_total_price
                print(f"\n✅  Added {quantity} {choice}(s) to cart.")
            else:
                print("\n⚠  Quantity must be greater than 0.")
        except ValueError:
            print("\n⚠  Invalid quantity. Please enter a valid number.")
    else:
        print("\n⚠  Item not available. Please choose from the menu.")
# Generate and print the final bill
print("\n" + "="*35)
print(" "*10 + "PYTHON SUPERMART")
print("="*35)
print(f"{'Item':<12} | {'Qty':<5} | {'Price':<10}")

print("-" * 35)
if not cart:
    print("Your cart is empty.")
else:
    for item in cart:
        # Formatting to align text properly
        print(f"{item[0].capitalize():<12} | {item[1]:<5} | ₹{item[2]:<10.2f}")
print("-" * 35)
print(f"{'Subtotal:':<21} ₹{total_amount:.2f}")
# Calculate a 5% tax
tax = total_amount * 0.05
print(f"{'Tax (5%):':<21} ₹{tax:.2f}")
print("-" * 35)
final_total = total_amount + tax
print(f"{'TOTAL DUE:':<21} ₹{final_total:.2f}")
print("="*35)
print("     Thank you for shopping!     ")
print("="*35)
