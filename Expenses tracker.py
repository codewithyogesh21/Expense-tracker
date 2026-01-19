expenses = []

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food/Travel/Study/etc): ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- Expense List ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - ₹{exp['amount']} ({exp['description']})")
    print()


def total_expense():
    total = 0
    for exp in expenses:
        total += exp["amount"]

    print("Total Expense: ₹", total, "\n")


def category_summary():
    summary = {}

    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    print("\n--- Category-wise Summary ---")
    for cat, amt in summary.items():
        print(cat, ":", amt)
    print()


while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.\n")
