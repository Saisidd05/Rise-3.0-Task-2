import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILE_NAME = "Expense tracker.csv"

# -----------------------------------
# Read CSV Data
# -----------------------------------
def read_data():
    data = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Amount"] = float(row["Amount"])
            data.append(row)
    return data

# -----------------------------------
# Filter Data
# -----------------------------------
def filter_data(data, person, month):
    return [
        row for row in data
        if row["Person"].lower() == person.lower()
        and row["Date"].startswith(month)
    ]

# -----------------------------------
# Income vs Expense Summary
# -----------------------------------
def income_vs_expense(data):
    income = 0
    expense = 0

    for row in data:
        if row["Type"] == "Income":
            income += row["Amount"]
        else:
            expense += row["Amount"]

    savings = income - expense

    print("\n💰 Income vs Expense Summary")
    print(f"Total Income  : ₹{income:.2f}")
    print(f"Total Expense : ₹{expense:.2f}")
    print(f"Savings       : ₹{savings:.2f}")

    return income, expense

# -----------------------------------
# Category-wise Expense Report
# -----------------------------------
def category_report(data):
    categories = defaultdict(float)

    for row in data:
        if row["Type"] == "Expense":
            categories[row["Category"]] += row["Amount"]

    print("\n📊 Category-wise Expenses")
    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt:.2f}")

    return categories

# -----------------------------------
# Plot Charts
# -----------------------------------
def plot_charts(categories, income, expense):
    print("\n1. Expense Pie Chart")
    print("2. Expense Bar Chart")
    print("3. Income vs Expense Bar Chart")

    choice = input("Choose chart: ")

    if choice == "1":
        plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
        plt.title("Expense Distribution")
        plt.show()

    elif choice == "2":
        plt.bar(categories.keys(), categories.values())
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")
        plt.title("Expenses by Category")
        plt.show()

    elif choice == "3":
        plt.bar(["Income", "Expense"], [income, expense])
        plt.ylabel("Amount (₹)")
        plt.title("Income vs Expense")
        plt.show()

# -----------------------------------
# Main Menu
# -----------------------------------
def main():
    data = read_data()

    while True:
        print("\n====== Budget Tracker CLI ======")
        print("1. Monthly Report (Student)")
        print("2. Monthly Report (Family)")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            month = input("Enter month (YYYY-MM): ")
            filtered = filter_data(data, "Student", month)

        elif choice == "2":
            month = input("Enter month (YYYY-MM): ")
            filtered = filter_data(data, "Family", month)

        elif choice == "3":
            print("👋 Exiting... Thank you!")
            break

        else:
            print("❌ Invalid choice")
            continue

        if not filtered:
            print("❌ No data found")
            continue

        income, expense = income_vs_expense(filtered)
        categories = category_report(filtered)
        plot_charts(categories, income, expense)

# -----------------------------------
# Run Program
# -----------------------------------
if __name__ == "__main__":
    main()
