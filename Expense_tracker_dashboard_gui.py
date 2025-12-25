import csv
from tkinter import *
from collections import defaultdict
import matplotlib.pyplot as plt
import os

FILE = "budget_data.csv"
REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

# Global storage
monthly_income = {}
monthly_expense = {}
category_expense = {}
current_person = ""
current_year = ""

# ---------------- Load Data ----------------
def load_data():
    with open(FILE, newline="", encoding="utf-8") as f:
        data = list(csv.DictReader(f))
        for r in data:
            r["Amount"] = float(r["Amount"])
        return data

# ---------------- Generate Report ----------------
def generate_report():
    global monthly_income, monthly_expense, category_expense
    global current_person, current_year

    person = person_var.get()
    year = year_var.get()
    current_person, current_year = person, year

    data = load_data()

    monthly_income = defaultdict(float)
    monthly_expense = defaultdict(float)
    category_expense = defaultdict(float)
    export_rows = []

    for r in data:
        if r["Date"][:4] != year:
            continue
        if person != "Both" and r["Person"] != person:
            continue

        export_rows.append(r)
        month = r["Date"][:7]

        if r["Type"] == "Income":
            monthly_income[month] += r["Amount"]
        else:
            monthly_expense[month] += r["Amount"]
            category_expense[r["Category"]] += r["Amount"]

    if not export_rows:
        summary.set("❌ No data found")
        return

    total_income = sum(monthly_income.values())
    total_expense = sum(monthly_expense.values())
    savings = total_income - total_expense

    summary.set(
        f"📅 Year: {year}\n"
        f"👤 Person: {person}\n\n"
        f"💰 Income   : ₹{total_income}\n"
        f"💸 Expense : ₹{total_expense}\n"
        f"💾 Savings : ₹{savings}"
    )

    # Export yearly report
    export_file = f"{REPORT_DIR}/{person.lower()}_{year}.csv"
    with open(export_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Date", "Person", "Type", "Category", "Amount", "Description"]
        )
        writer.writeheader()
        writer.writerows(export_rows)

# ---------------- Show Graph ----------------
def show_graph():
    if not monthly_expense:
        summary.set("⚠ Generate report first")
        return

    graph = graph_var.get()
    months = sorted(monthly_expense.keys())

    if graph == "Monthly Expense":
        values = [monthly_expense[m] for m in months]
        plt.bar(months, values, color="#4cc9f0")
        plt.xticks(rotation=45)
        plt.title("Monthly Expense Comparison")
        plt.ylabel("Amount (₹)")

    elif graph == "Category Pie":
        plt.pie(category_expense.values(),
                labels=category_expense.keys(),
                autopct="%1.1f%%")
        plt.title("Category-wise Expenses")

    elif graph == "Savings Trend":
        savings = [
            monthly_income[m] - monthly_expense[m] for m in months
        ]
        plt.plot(months, savings, marker="o", color="#4ade80")
        plt.xticks(rotation=45)
        plt.title("Savings Trend")
        plt.ylabel("Savings (₹)")
        plt.grid(True)

    elif graph == "Forecast (Next Year)":
        forecast_next_year()

    plt.tight_layout()
    plt.show()

# ---------------- Forecast Logic ----------------
def forecast_next_year():
    months = sorted(monthly_expense.keys())
    expenses = [monthly_expense[m] for m in months]

    if len(expenses) < 2:
        summary.set("⚠ Not enough data for forecasting")
        return

    avg_growth = (expenses[-1] - expenses[0]) / len(expenses)

    forecast = []
    last_value = expenses[-1]

    for _ in range(12):
        last_value += avg_growth
        forecast.append(round(last_value, 2))

    plt.plot(range(1, 13), forecast, marker="o", color="#f59e0b")
    plt.title(f"Forecasted Monthly Expenses ({int(current_year)+1})")
    plt.xlabel("Month")
    plt.ylabel("Predicted Expense (₹)")
    plt.grid(True)

# ---------------- Reset ----------------
def reset_dashboard():
    summary.set("")
    person_var.set("Student")
    year_var.set("2020")
    graph_var.set("Monthly Expense")
    monthly_expense.clear()
    monthly_income.clear()
    category_expense.clear()

# ---------------- GUI ----------------
root = Tk()
root.title("📊 Expense Tracker Dashboard")
root.geometry("650x620")
root.configure(bg="#0f172a")

Label(root, text="Expense Tracker Dashboard",
      font=("Segoe UI", 20, "bold"),
      fg="#38bdf8", bg="#0f172a").pack(pady=15)

panel = Frame(root, bg="#1e293b")
panel.pack(padx=30, pady=10, fill="both", expand=True)

# Selectors
Label(panel, text="Person", fg="white", bg="#1e293b").pack()
person_var = StringVar(value="Student")
OptionMenu(panel, person_var, "Student", "Family", "Both").pack()

Label(panel, text="Year", fg="white", bg="#1e293b").pack(pady=(10, 0))
year_var = StringVar(value="2020")
OptionMenu(panel, year_var, "2020", "2021", "2022", "2023", "2024").pack()

# Buttons
Button(panel, text="📄 Generate Report",
       bg="#38bdf8", font=("Segoe UI", 11, "bold"),
       command=generate_report).pack(fill="x", padx=40, pady=10)

Label(panel, text="Select Graph", fg="white", bg="#1e293b").pack(pady=(10, 0))
graph_var = StringVar(value="Monthly Expense")
OptionMenu(panel, graph_var,
           "Monthly Expense",
           "Category Pie",
           "Savings Trend",
           "Forecast (Next Year)").pack()

Button(panel, text="📊 Show Selected Graph",
       bg="#fbbf24",
       command=show_graph).pack(fill="x", padx=40, pady=10)

Button(panel, text="🔄 Reset",
       bg="#e5e7eb",
       command=reset_dashboard).pack(fill="x", padx=40, pady=5)

# Summary
summary = StringVar()
Label(panel, textvariable=summary,
      bg="#020617", fg="#4ade80",
      font=("Consolas", 12),
      justify=LEFT, padx=20, pady=20).pack(fill="x", padx=20, pady=20)

Label(root, text="Python • Tkinter • CSV • Forecasting • Dashboard",
      fg="#64748b", bg="#0f172a",
      font=("Segoe UI", 9)).pack(pady=8)

root.mainloop()
