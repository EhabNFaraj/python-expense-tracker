# Python Expense Tracker 📊

A command-line personal expense tracker built in Python. Logs expenses by category, tracks monthly spending against budgets, and visualizes data with Matplotlib.

## 💡 Features

- Add expenses by category and amount
- Input validation — prevents crashes from invalid entries
- View total expenses summary (all time)
- View monthly expense summary with budget usage %
- Budget warnings — alerts at 50%, 80%, and 100% of limit
- Save to a local CSV file (expenses.csv)
- Generate colorful bar chart with spending labels

## 🔔 Budget Warning System

| Usage | Alert |
|-------|-------|
| 50%+  | 📊 Heads up |
| 80%+  | ⚠️ Warning |
| 100%+ | 🚨 Over budget |

## 🛠️ Tech Used

- Python 3
- CSV (built-in)
- Matplotlib (pip install matplotlib)

## ▶️ How to Run

1. Make sure Python is installed
2. Install matplotlib: pip install matplotlib
3. Run the program: python Expense_Tracker.py

## 📋 Menu Options

1. Log Expense
2. View Summary (All Time)
3. View Monthly Summary
4. Show Chart
5. Exit

## 📁 Default Budget Limits

| Category      | Budget |
|---------------|--------|
| Food          | $500   |
| Rent          | $1,500 |
| Insurance     | $200   |
| Phone Bill    | $100   |
| Gas           | $200   |
| Entertainment | $150   |
| Other         | $300   |
