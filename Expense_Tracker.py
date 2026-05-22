import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Budget limits per category
BUDGET_LIMITS = {
    "food": 500,
    "rent": 1500,
    "insurance": 200,
    "phone bill": 100,
    "gas": 200,
    "entertainment": 150,
    "other": 300
}

CATEGORIES = ["Food", "Rent", "Insurance", "Phone Bill", "Gas", "Entertainment", "Other"]

# Function to log an expense
def log_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    
    print("\n📋 Available Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    
    category = input("\nEnter expense category (or type your own): ").strip()
    
    # Input validation for amount
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("❌ Amount must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid amount. Please enter a number (e.g., 50 or 49.99).")

    with open("Expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category.lower(), amount])

    print(f"✅ Expense logged! ${amount:.2f} for {category}")

    # Budget warning check
    check_budget(category.lower())

# Function to check budget warnings
def check_budget(category):
    category = category.lower()
    if category not in BUDGET_LIMITS:
        return
    
    total = 0
    current_month = datetime.now().strftime("%Y-%m")
    
    try:
        with open("Expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                if row[0].startswith(current_month) and row[1].lower() == category:
                    total += float(row[2])
        
        limit = BUDGET_LIMITS[category]
        percentage = (total / limit) * 100

        if percentage >= 100:
            print(f"🚨 OVER BUDGET! You've spent ${total:.2f} of your ${limit} {category.title()} budget this month!")
        elif percentage >= 80:
            print(f"⚠️  Warning! You've used {percentage:.0f}% (${total:.2f}/${limit}) of your {category.title()} budget this month.")
        elif percentage >= 50:
            print(f"📊 Heads up: You've used {percentage:.0f}% (${total:.2f}/${limit}) of your {category.title()} budget this month.")
    except FileNotFoundError:
        pass

# Function to show total per category
def show_summary():
    expenses = {}
    try:
        with open("Expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                category = row[1].title()
                amount = float(row[2])
                expenses[category] = expenses.get(category, 0) + amount

        if not expenses:
            print("No expenses found yet.")
            return

        print("\n📊 Expense Summary (All Time):")
        print("-" * 40)
        for category, total in sorted(expenses.items()):
            limit = BUDGET_LIMITS.get(category.lower(), None)
            if limit:
                percentage = (total / limit) * 100
                print(f"  {category:<20} ${total:.2f} / ${limit} budget ({percentage:.0f}%)")
            else:
                print(f"  {category:<20} ${total:.2f}")
        print("-" * 40)
        print(f"  {'TOTAL':<20} ${sum(expenses.values()):.2f}")

    except FileNotFoundError:
        print("No expenses found yet. Please log an expense first.")

# Function to show monthly summary
def show_monthly_summary():
    month_input = input("Enter month to view (YYYY-MM), or press Enter for current month: ").strip()
    if not month_input:
        month_input = datetime.now().strftime("%Y-%m")

    expenses = {}
    try:
        with open("Expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                if row[0].startswith(month_input):
                    category = row[1].title()
                    amount = float(row[2])
                    expenses[category] = expenses.get(category, 0) + amount

        if not expenses:
            print(f"No expenses found for {month_input}.")
            return

        print(f"\n📅 Expense Summary for {month_input}:")
        print("-" * 40)
        for category, total in sorted(expenses.items()):
            limit = BUDGET_LIMITS.get(category.lower(), None)
            if limit:
                percentage = (total / limit) * 100
                print(f"  {category:<20} ${total:.2f} / ${limit} budget ({percentage:.0f}%)")
            else:
                print(f"  {category:<20} ${total:.2f}")
        print("-" * 40)
        print(f"  {'TOTAL':<20} ${sum(expenses.values()):.2f}")

    except FileNotFoundError:
        print("No expenses found yet. Please log an expense first.")

# Function to show chart
def show_chart():
    categories = []
    amounts = []
    try:
        with open("Expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:
                    continue
                category = row[1].title()
                amount = float(row[2])
                if category in categories:
                    idx = categories.index(category)
                    amounts[idx] += amount
                else:
                    categories.append(category)
                    amounts.append(amount)

        if categories:
            colors = ['#2E86C1', '#E67E22', '#27AE60', '#8E44AD', '#E74C3C', '#F39C12', '#1ABC9C', '#95A5A6']
            plt.figure(figsize=(10, 6))
            bars = plt.bar(categories, amounts, color=colors[:len(categories)])
            plt.title("Expenses by Category", fontsize=14, fontweight='bold')
            plt.xlabel("Category", fontsize=12)
            plt.ylabel("Amount ($)", fontsize=12)
            
            for bar, amount in zip(bars, amounts):
                plt.text(bar.get_x() + bar.get_width()/2., bar.get_height(),
                        f'${amount:.0f}', ha='center', va='bottom', fontweight='bold')
            
            plt.tight_layout()
            plt.show()
        else:
            print("No data to show.")
    except FileNotFoundError:
        print("No expenses found yet. Please log an expense first.")

# Function to clear all data
def clear_data():
    confirm = input("⚠️  Are you sure you want to clear ALL expense data? (yes/no): ").strip().lower()
    if confirm == "yes":
        with open("Expenses.csv", mode="w", newline="") as file:
            pass
        print("✅ All expense data has been cleared.")
    else:
        print("❌ Clear cancelled.")

# Menu system
def main():
    while True:
        print("\n💼 Expense Tracker Menu")
        print("1. Log Expense")
        print("2. View Summary (All Time)")
        print("3. View Monthly Summary")
        print("4. Show Chart")
        print("5. Clear All Data")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            log_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_monthly_summary()
        elif choice == "4":
            show_chart()
        elif choice == "5":
            clear_data()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the program
main()
