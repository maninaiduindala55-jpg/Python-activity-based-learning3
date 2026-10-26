initial_balance = 1000.00
balance = initial_balance
transactions = []

choice = "yes"

while choice == "yes":
    transaction_type = input("Enter transaction type (withdrawal/deposit): ").lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount.")

        transactions.append((transaction_type, amount, "Rejected"))

    elif transaction_type == "withdrawal":
        if amount > balance:
            print("Insufficient balance for withdrawal.")

            transactions.append((transaction_type, amount, "Rejected"))
        else:
            balance -= amount

            transactions.append((transaction_type, amount, "Successful"))

            print("Withdrawal successful.")
            print("Remaining balance: ₹", balance)

    elif transaction_type == "deposit":
        balance += amount

        transactions.append((transaction_type, amount, "Successful"))

        print("Deposit successful.")
        print("Updated balance: ₹", balance)

    else:
        print("Invalid transaction type.")

        transactions.append((transaction_type, amount, "Rejected"))

    choice = input("Do you want to perform another transaction? (yes/no): ").lower()

print("\n--- ATM TRANSACTION SUMMARY ---")
print(f"Initial balance: ₹ {initial_balance}")

print("\nTransaction History:")

for transaction in transactions:
    print(transaction)

print("\nFinal balance: ₹", balance)
print("Thank you for using the ATM!")