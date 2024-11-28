import json
from datetime import datetime

# Initialize data storage
expense_data = []

# Function to add an expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
        expense = {
            "date": date,
            "amount": amount,
            "description": description,
            "category": category
        }
        expense_data.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Please enter the correct data.")

# Function to view all expenses
def view_expenses():
    if not expense_data:
        print("No expenses recorded yet!")
    else:
        for idx, expense in enumerate(expense_data, start=1):
            print(f"{idx}. Date: {expense['date']}, Amount: {expense['amount']}, "
                  f"Description: {expense['description']}, Category: {expense['category']}")

# Function to view summary by category
def view_category_summary():
    category_summary = {}
    for expense in expense_data:
        category = expense["category"]
        category_summary[category] = category_summary.get(category, 0) + expense["amount"]
    
    print("\nCategory-wise Summary:")
    for category, total in category_summary.items():
        print(f"{category}: {total}")

# Function to view monthly summary
def view_monthly_summary():
    monthly_summary = {}
    for expense in expense_data:
        month = datetime.strptime(expense["date"], "%Y-%m-%d").strftime("%Y-%m")
        monthly_summary[month] = monthly_summary.get(month, 0) + expense["amount"]
    
    print("\nMonthly Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: {total}")

# Function to save data to a file
def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expense_data, file)
    print("Data saved to expenses.json!")

# Function to load data from a file
def load_data():
    global expense_data
    try:
        with open("expenses.json", "r") as file:
            expense_data = json.load(file)
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")

# Main menu
def main():
    load_data()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. View Category-wise Summary")
        print("4. View Monthly Summary")
        print("5. Save Data")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_category_summary()
        elif choice == "4":
            view_monthly_summary()
        elif choice == "5":
            save_data()
        elif choice == "6":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

