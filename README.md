# expense-analysis-2023

## 🏢 Example Company Description

The company is a mid-sized **tech and professional services firm** with around **300 employees**. It provides **custom software development**, **IT consulting**, and **marketing strategy services** for clients across industries.  
The organization has five core departments:  

- **Engineering** – Handles software and product development projects for clients.  
- **Marketing** – Manages client marketing campaigns, digital advertising, branding, and internal promotions.  
- **Sales** – Focuses on acquiring new clients, managing relationships, and attending industry events.  
- **Human Resources (HR)** – Oversees hiring, employee training, and benefits administration.  
- **Information Technology (IT)** – Supports the internal tech infrastructure and client IT implementations.

The company works both **remotely and in-office**, with travel required for client meetings, conferences, and trainings.

---

## 💼 Business Scenario: Expense Review for Finance Team

You’re a **data analyst** at a mid-sized company. The **finance department** has asked you to **explore internal expense records** from the past year.

Their goal is to **better understand how different departments are spending money** and to **identify any early red flags or cost-saving opportunities**.  
You’ve been provided with a **raw expense table** that includes details like **date, department, category, employee, vendor, and amount**.

---

## 📊 Project Goals

- Understand how each department is spending money.
- Spot unusual spending patterns or cost-saving opportunities.
- Provide clear visuals and actionable insights for the finance team.
  
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

- Sales spends less than expected on Meals but more on Software.
- Some spikes in Sales transactions suggest one-off costs worth reviewing.
- Engineering shows higher spend on Training and Office Supplies than peers.
  
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

- Department spending vs. company averages (z-scores)
- Outlier detection on transactions
- Large transactions flagged for review
- Monthly trends & spikes
- Department/category breakdown with deviation from expected benchmarks





   
