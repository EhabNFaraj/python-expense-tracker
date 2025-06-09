import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Function to log an expense
def log_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter expense category (e.g., Food, Rent, etc.): ")
    amount = input("Enter amount: ")

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print("✅ Expense logged!")

# Function to show total per category
def show_summary():
    expenses = {}

    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                category = row[1]
                amount = float(row[2])
                expenses[category] = expenses.get(category, 0) + amount

        print("\n📊 Expense Summary:")
        for category, total in expenses.items():
            print(f"{category}: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses found yet. Please log an expense first.")

# Function to show chart
def show_chart():
    categories = []
    amounts = []

    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                category = row[1]
                amount = float(row[2])
                if category in categories:
                    idx = categories.index(category)
                    amounts[idx] += amount
                else:
                    categories.append(category)
                    amounts.append(amount)

        if categories:
            plt.bar(categories, amounts)
            plt.title("Expenses by Category")
            plt.xlabel("Category")
            plt.ylabel("Amount ($)")
            plt.show()
        else:
            print("No data to show.")
    except FileNotFoundError:
        print("No expenses found yet. Please log an expense first.")

# Menu system
def main():
    while True:
        print("\n💼 Expense Tracker Menu")
        print("1. Log Expense")
        print("2. View Summary")
        print("3. Show Chart")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            log_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_chart()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the program
main()
