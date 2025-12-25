# 💸 Expense Tracker Dashboard (Python)

A Python-based **Expense Tracker and Budget Analysis Dashboard** that helps analyze **income, expenses, savings, and future trends** using real-world data.
The project supports **Student, Family, and Combined (Both)** budgeting with **graphical visualization and forecasting**.

---

## 🚀 Features

* 📊 **Dashboard-style GUI** using Tkinter
* 👤 **Person-wise analysis**: Student / Family / Both
* 📅 **Year-wise filtering** (2020–2024)
* 📈 **Monthly expense comparison (Jan–Dec)**
* 🥧 **Category-wise expense pie chart**
* 💾 **Savings trend analysis**
* 🔮 **Next-year expense forecasting** (trend-based prediction)
* 📁 **CSV export of reports**
* 🎨 Clean, user-friendly interface

---

## 🧠 Forecasting Approach

The forecasting feature predicts **next year’s monthly expenses** using historical trends:

* Calculates overall expense growth from past years
* Applies average growth to estimate future monthly expenses
* Displays results using a line graph

This method is **simple, explainable, and suitable for academic projects**.

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI development
* **CSV** – Data storage
* **Matplotlib** – Graphs and visualization
* **Collections (defaultdict)** – Data aggregation

---

## 📁 Project Structure

```
ExpenseTracker/
│
├── budget_data.csv                 # 5 years of auto-generated data
├── expense_tracker_dashboard.py    # Main dashboard application
├── generate_budget_data.py         # Script to auto-generate data
├── reports/                        # Exported CSV reports
└── README.md
```

---

## ▶ How to Run the Project

### 1️⃣ Install required libraries

```bash
pip install matplotlib
```

### 2️⃣ (Optional) Generate dataset

```bash
python generate_budget_data.py
```

### 3️⃣ Run the dashboard

```bash
python expense_tracker_dashboard.py
```

---

## 📊 How to Use

1. Select **Person** (Student / Family / Both)
2. Select **Year**
3. Click **Generate Report**
4. Choose a **Graph Type**
5. Click **Show Selected Graph**
6. Export report if needed

---

## 🎓 Academic Relevance

This project demonstrates:

* File handling using CSV
* Data analysis and aggregation
* GUI application development
* Graphical data visualization
* Trend-based forecasting
* Real-world budgeting concepts

It is suitable for:

* College mini projects
* Python lab submissions
* Data analysis demonstrations

---

## 📌 Future Enhancements

* PDF report export
* Income forecasting
* Machine learning–based prediction
* Database integration (SQLite)
* Login-based user system

---

## 👨‍💻 Author

**Sai Siddharth Nanda Gopal**
Python | Data Analysis | GUI Development

---
Just tell me 👌
