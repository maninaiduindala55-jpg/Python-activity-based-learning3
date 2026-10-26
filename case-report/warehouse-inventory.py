
number_of_products = int(input("Enter the number of products: "))

for i in range(number_of_products):
    print("\nProduct", i + 1)

    product_name = input("Enter product name: ")
    opening_stock = int(input("Enter opening stock: "))
    incoming_quantity = int(input("Enter incoming quantity: "))
    dispatched_quantity = int(input("Enter dispatched quantity: "))
    actual_closing_stock = int(input("Enter actual closing stock: "))
    target_stock_level = int(input("Enter target stock level: "))

    expected_closing_stock = (opening_stock + incoming_quantity - dispatched_quantity)

    print("\nProduct Name:", product_name)
    print("Expected Closing Stock:", expected_closing_stock)
    print("Actual Closing Stock:", actual_closing_stock)

    if actual_closing_stock == expected_closing_stock:
        print("Status: No Discrepancy")

    elif actual_closing_stock < expected_closing_stock:
        shortage = expected_closing_stock - actual_closing_stock
        print("Status: Shortage")
        print("Shortage Quantity:", shortage)

    else:
        surplus = actual_closing_stock - expected_closing_stock
        print("Status: Surplus")
        print("Surplus Quantity:", surplus)

    replenishment_quantity = max(0, target_stock_level - actual_closing_stock)

    print("Target Stock Level:", target_stock_level)
    print("Replenishment Quantity:", replenishment_quantity)

print("\nInventory reconciliation completed.")