# expense-analysis

## 🏢 Example Company Description

The company is a small, specialized tech and professional services firm run by a lean team of six core employees. This tight-knit group handles custom software development, IT support, marketing campaigns, sales operations, and HR tasks for a range of clients across industries.

Because the company is small and agile, each employee wears multiple hats — working across departments to manage different projects, budgets, and client needs. As a result, all six employees are expected to share spending responsibilities equally — meaning their expenses should generally be balanced across departments and categories.

The organization maintains clear expense policies to keep spending in check while balancing remote and in-office work, plus regular travel for client meetings, conferences, and training.

---

💼 Business Scenario: Expense Review for Finance

You’re the sole data analyst supporting this small team. The finance lead has asked you to analyze the company’s expense records from the past year to spot early red flags, policy violations, or cost-saving opportunities.

You’ve been given a raw expense file that includes details like date, department, category, employee, vendor, and amount — all linked back to the same six employees who spend across every department.

Your goal is to turn this data into clear, actionable insights that help the team spend wisely and stick to budget as they grow — while flagging any spending patterns that look significantly above or below the fair share expected for each employee.

---

## 📁 Folder Structure
/Expenses-Analysis-Project
├─ data/               # Raw CSV expense data
├─ scripts/            # Python scripts for analysis
├─ charts/             # Saved visuals (optional)
├─ notebooks/          # If you have Jupyter notebooks
├─ README.md           # This file
└─ requirements.txt    # Python 

---

## 📊 Analysis Overview

This project explores departmental spending trends and flags potential outliers.

**Key scripts:**
- `scripts/monthly_trends.py`: Analyzes spend by month for trends and outliers.
- `scripts/large_transactions.py`: Pulls largest transactions by department.
- `scripts/global_outliers.py`: Flags unusual transactions across the dataset.
- `scripts/monthly_dept_zscores.py`: Compares monthly spend with z-scores by department.
- `scripts/dept_spend_outliers.py`: Combines department-level spend, averages, and outlier rates.

Visuals are saved in the `charts/` folder for easy review.

This project uses Python, DuckDB, pandas, and visualization libraries to:
- Calculate spending trends by month.
- Find outliers across departments and categories.
- Visualize expense patterns with heatmaps and scatter plots.
- Benchmark department spending against company averages and custom tiers.

---

## 🔑 Key Insights


  
---

## 🛠️ How It Works 



---

## 🚀 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Expenses-Analysis-2023.git
   cd Expenses-Analysis-2023
   ```
   
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run an analyst script**
   ```bash
   python scripts/your_script_name.py
   ```
   
---

## ✅ Insights Covered







   
