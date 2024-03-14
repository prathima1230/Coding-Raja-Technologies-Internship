import json
import os

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def add_income(data):
    amount = float(input("Enter income amount in rupees: "))
    data['income'] += amount
    print("Income added successfully.")

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount in rupees: "))
    data['expenses'].append({'category': category, 'amount': amount})
    print("Expense added successfully.")

def calculate_budget(data):
    total_expenses = sum(item['amount'] for item in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    return remaining_budget

def analyze_expenses(data):
    expense_categories = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    print("Expense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ₹{amount:.2f}")

def erase_data(filename):
    confirmation = input("Are you sure you want to erase all data? (yes/no): ")
    if confirmation.lower() == 'yes':
        with open(filename, 'w') as file:
            file.write('')
        print("All data erased successfully.")
    else:
        print("Operation canceled.")

def main():
    filename = "budget_data.json"
    data = load_data(filename)

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Erase All Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            remaining_budget = calculate_budget(data)
            print(f"Remaining Budget: ₹{remaining_budget:.2f}")
        elif choice == '4':
            analyze_expenses(data)
        elif choice == '5':
            erase_data(filename)
            data = {'income': 0, 'expenses': []}  # Reset data in memory
        elif choice == '6':
            save_data(data, filename)
            print("Exiting... Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()