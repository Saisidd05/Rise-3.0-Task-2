import csv
import random
from datetime import date

FILE = "Expense tracker.csv"

years = range(2020, 2025)
months = range(1, 13)

student_expenses = {
    "Food": (800, 1300),
    "Travel": (300, 600),
    "Education": (600, 2000),
    "Entertainment": (300, 800),
    "Utilities": (200, 500),
    "Shopping": (300, 1200)
}

family_expenses = {
    "Rent": (10000, 14000),
    "Groceries": (3000, 5000),
    "Utilities": (1500, 2500),
    "Transport": (2000, 3500),
    "Education": (2000, 4000),
    "Healthcare": (1000, 3000),
    "Entertainment": (1500, 4000)
}

with open(FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Person", "Type", "Category", "Amount", "Description"])

    for y in years:
        for m in months:
            month_date = f"{y}-{m:02d}-01"

            # -------- Student Income --------
            writer.writerow([
                month_date, "Student", "Income", "Allowance",
                random.randint(4500, 6500),
                "Monthly allowance"
            ])

            # -------- Student Expenses --------
            for cat, (low, high) in student_expenses.items():
                writer.writerow([
                    month_date, "Student", "Expense", cat,
                    random.randint(low, high),
                    f"{cat} expense"
                ])

            # -------- Family Income --------
            writer.writerow([
                month_date, "Family", "Income", "Salary",
                random.randint(35000, 55000),
                "Monthly salary"
            ])

            # -------- Family Expenses --------
            for cat, (low, high) in family_expenses.items():
                writer.writerow([
                    month_date, "Family", "Expense", cat,
                    random.randint(low, high),
                    f"{cat} expense"
                ])

print("✅ Budget_data.csv generated successfully!")

