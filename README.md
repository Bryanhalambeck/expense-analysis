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

# 💼 Sales Department – Office Supplies Expense Analysis

This project analyzes expense transactions from a small company to identify potential red flags, imbalances, and opportunities for oversight improvement — focusing specifically on the **Sales department's Office Supplies spending**. The goal was to surface actionable insights using real-world data analysis techniques and custom benchmarks.

---

## 🔍 Project Summary

- **Department Focus**: Sales  
- **Category Analyzed**: Office Supplies  
- **Dataset**: Internal transactions with columns like `date`, `employee`, `vendor`, `amount`, `category`, `department`  
- **Tools Used**: Python, Pandas, DuckDB, Seaborn, Matplotlib, Z-score analysis, Custom benchmarking

---

## 📈 Key Insights

- **⚠️ Single Outlier Transaction**:  
  One purchase in May 2025 ($972.45 at Staples) accounted for **over 40%** of the Sales department’s annual spend in this category — standing more than **2.2 standard deviations above** the norm.

- **👤 Employee-Level Imbalance**:  
  David Kim alone accounted for over **40% of total spend** — a potential sign of informal role specialization or policy drift. Frank Wu, by contrast, spent **over 1 SD below** the team average.

- **🏪 Vendor Concentration**:  
  Staples received 60% of total spend and was flagged as a **vendor-level outlier** (z > 1.5). This concentration may reflect a preferred supplier or warrant a pricing/policy review.

- **📅 Timing Irregularities**:  
  Transactions occurred on a **Saturday** and **two holidays**, which may require review for proper policy adherence.

- **📊 Benchmark Deviation**:  
  Sales had the **largest deviation (+28.3)** from expected Office Supplies spending compared to all other departments and categories — based on a custom benchmark system.

---

## 📂 Repository Structure
# 💼 Sales Department – Office Supplies Expense Analysis

This project analyzes expense transactions from a small company to identify potential red flags, imbalances, and opportunities for oversight improvement — focusing specifically on the **Sales department's Office Supplies spending**. The goal was to surface actionable insights using real-world data analysis techniques and custom benchmarks.

---

## 🔍 Project Summary

- **Department Focus**: Sales  
- **Category Analyzed**: Office Supplies  
- **Dataset**: Internal transactions with columns like `date`, `employee`, `vendor`, `amount`, `category`, `department`  
- **Tools Used**: Python, Pandas, DuckDB, Seaborn, Matplotlib, Z-score analysis, Custom benchmarking

---

## 📈 Key Insights

- **⚠️ Single Outlier Transaction**:  
  One purchase in May 2025 ($972.45 at Staples) accounted for **over 40%** of the Sales department’s annual spend in this category — standing more than **2.2 standard deviations above** the norm.

- **👤 Employee-Level Imbalance**:  
  David Kim alone accounted for over **40% of total spend** — a potential sign of informal role specialization or policy drift. Frank Wu, by contrast, spent **over 1 SD below** the team average.

- **🏪 Vendor Concentration**:  
  Staples received 60% of total spend and was flagged as a **vendor-level outlier** (z > 1.5). This concentration may reflect a preferred supplier or warrant a pricing/policy review.

- **📅 Timing Irregularities**:  
  Transactions occurred on a **Saturday** and **two holidays**, which may require review for proper policy adherence.

- **📊 Benchmark Deviation**:  
  Sales had the **largest deviation (+28.3)** from expected Office Supplies spending compared to all other departments and categories — based on a custom benchmark system.

---

## 📂 Repository Structure
# 💼 Sales Department – Office Supplies Expense Analysis

This project analyzes expense transactions from a small company to identify potential red flags, imbalances, and opportunities for oversight improvement — focusing specifically on the **Sales department's Office Supplies spending**. The goal was to surface actionable insights using real-world data analysis techniques and custom benchmarks.

---

## 🔍 Project Summary

- **Department Focus**: Sales  
- **Category Analyzed**: Office Supplies  
- **Dataset**: Internal transactions with columns like `date`, `employee`, `vendor`, `amount`, `category`, `department`  
- **Tools Used**: Python, Pandas, DuckDB, Seaborn, Matplotlib, Z-score analysis, Custom benchmarking

---

## 📈 Key Insights

- **⚠️ Single Outlier Transaction**:  
  One purchase in May 2025 ($972.45 at Staples) accounted for **over 40%** of the Sales department’s annual spend in this category — standing more than **2.2 standard deviations above** the norm.

- **👤 Employee-Level Imbalance**:  
  David Kim alone accounted for over **40% of total spend** — a potential sign of informal role specialization or policy drift. Frank Wu, by contrast, spent **over 1 SD below** the team average.

- **🏪 Vendor Concentration**:  
  Staples received 60% of total spend and was flagged as a **vendor-level outlier** (z > 1.5). This concentration may reflect a preferred supplier or warrant a pricing/policy review.

- **📅 Timing Irregularities**:  
  Transactions occurred on a **Saturday** and **two holidays**, which may require review for proper policy adherence.

- **📊 Benchmark Deviation**:  
  Sales had the **largest deviation (+28.3)** from expected Office Supplies spending compared to all other departments and categories — based on a custom benchmark system.

---

## 📂 Repository Structure
project-folder/
│
├── scripts/
│   └── 01_sales_office_supplies_analysis.py        # Full analysis script
│
├── data/
│   └── Untitledspreadsheet72.csv                   # Cleaned expense data
│
├── charts/
│   ├── monthly_spend.png
│   ├── vendor_pie_chart.png
│   ├── zscore_outlier_plot.png
│   └── benchmark_heatmap.png
│
└── README.md                                        # Project overview and insights

---

## 📌 What I Planned (But Didn't Finish)

Originally, I planned to extend this analysis to cover:

- **Full Company Policy Check** (all departments/categories)
- **Same-Day Vendor Flagging**
- **Full Vendor Benchmarking**
- **Departmental Timing Patterns**

Due to time constraints, I focused instead on building a strong, polished deep dive into the Sales department — but I included my broader plan here to show my workflow and thought process.

---

## 🧠 Skills Demonstrated

- Real-world anomaly detection using z-scores
- Custom business benchmarking logic
- Transaction filtering and aggregation
- Visual storytelling with charts
- SQL-like analysis using DuckDB in Python
- Communicating complex insights clearly

---

## 🎥 Optional: Loom Video (if added)

[Watch the walk-through →](https://loom.com/your-link-here)

---

## ✍️ Author

**Bryan H.**  
Aspiring Data Analyst focused on business intelligence, expense optimization, and operational insight.

  





   






   
