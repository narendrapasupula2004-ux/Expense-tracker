import json, os

print("Current directory:", os.getcwd())

# Load old data if file exists
if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
else:
    expenses = {}

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")

    if category in expenses:
        expenses[category]['amount'] += amount
        expenses[category]['details'].append(desc)
    else:
        expenses[category] = {'amount': amount, 'details': [desc]}
    print("Expense added ✅")

def view_expenses():
    print("\n--- Expense Summary ---")
    total = 0
    for cat, info in expenses.items():
        print(f"{cat.capitalize():10} ₹{info['amount']:>7}   {info['details']}")
        total += info['amount']
    print(f"\nTotal Spending: ₹{total}")

def save_data():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)
    print("Data saved ✅")

while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Save and Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        save_data()
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice, try again.")
