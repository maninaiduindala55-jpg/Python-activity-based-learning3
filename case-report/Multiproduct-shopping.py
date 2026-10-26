budget = float(input("Enter shopping budget: Rs. "))
n = int(input("Enter number of products: "))

if budget <= 0:
    print("Invalid budget")
elif n <= 0:
    print("Invalid number of products")
else:
    total_cost = 0
    valid = True

    for i in range(n):
        name = input("Enter product name: ")
        price = float(input("Enter price per unit: Rs. "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid product details")
            valid = False
            break

        product_cost = price * quantity
        total_cost += product_cost

        print("Product:", name)
        print("Product cost: Rs.", round(product_cost, 2))
    if valid:
        print("Total shopping cost: Rs.", round(total_cost, 2))

        if total_cost <= budget:
            remaining = budget - total_cost
            print("Shopping is within budget")
            print("Remaining budget: Rs.", round(remaining, 2))
        else:
            excess = total_cost - budget
            print("Budget exceeded")
            print("Excess amount: Rs.", round(excess, 2))