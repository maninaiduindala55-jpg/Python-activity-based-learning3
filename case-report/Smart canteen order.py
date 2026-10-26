menu = {
    "Burger": {"price": 80, "stock": 10},
    "Sandwich": {"price": 50, "stock": 8},
    "Pizza": {"price": 120, "stock": 5},
    "Juice": {"price": 30, "stock": 12}
}

print("SMART CANTEEN ORDER AND STOCK MANAGEMENT")
print("\nAvailable Menu:")
for item, details in menu.items():
    print(item, "- Price: Rs.", details["price"],
          "| Stock:", details["stock"])

item_name = input("\nEnter food item: ").title()

if item_name not in menu:
    print("Invalid food item")
else:
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity")

    elif quantity > menu[item_name]["stock"]:
        print("Insufficient stock")

    else:
        total_bill = menu[item_name]["price"] * quantity

        menu[item_name]["stock"] -= quantity

        print("\nOrder placed successfully!")
        print("Food Item:", item_name)
        print("Quantity:", quantity)
        print("Total Bill: Rs.", total_bill)
        print("Remaining Stock:",
              menu[item_name]["stock"])