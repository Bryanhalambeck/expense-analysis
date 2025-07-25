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

# 📊 Category-Level Benchmarking (All Departments)

This section evaluates how each department’s spending behavior aligns with expectations across categories like Travel, Meals, and Office Supplies.

Using a custom benchmarking system, we:
- Calculate what % of each department's budget went to each category
- Compare that to what’s typical across departments
- Define “expected” spending tiers (low, medium, high) for each category
- Visualize how far off each department is from those expectations using a color-coded heatmap

This approach flags misalignments and potential budget issues that wouldn’t show up in raw totals alone.

---

## 📊 Benchmarking Logic Explained

To help identify which department-category pairs might warrant deeper investigation, I built a custom benchmarking system. This system scores each department based on how closely its spending aligns with expectations.

Here’s how it works:

### ✅ Step-by-Step Logic

1. **% of Department Spend by Category**  
   For each department, I calculated the percentage of their total budget spent in each category (Meals, Travel, etc.):

   $begin:math:display$
   \\text{Percent} = \\left( \\frac{\\text{Category Spend}}{\\text{Total Dept Spend}} \\right) \\times 100
   $end:math:display$

   This gives a normalized view of each department’s spending priorities.

2. **Deviation from Category Average**  
   I then subtracted the company-wide average for each category:

   $begin:math:display$
   \\text{Deviation} = \\text{This Dept’s %} - \\text{Category Average %}
   $end:math:display$

   This tells us how unusually high or low a department is spending in each area.

3. **Tier Midpoints from Percentiles**  
   I split all deviation values into percentile-based tiers:
   - Bottom 33% → **Low**
   - Middle 33% → **Medium**
   - Top 33% → **High**

   I also calculated “in-between” tier midpoints:
   - Medium–Low = avg of Low and Medium
   - Medium–High = avg of Medium and High

   These midpoints serve as numeric benchmarks for expected spending behavior.

4. **Manual Tier Expectations**  
   I manually defined what tier each department *should* be in for each category, based on company policy, logic, or business needs.  
   (e.g., Sales is expected to spend “Low” on Office Supplies, “High” on Travel.)

5. **Deviation from Expected Benchmark**  
   I then compared each department’s actual deviation to its expected tier midpoint:

   $begin:math:display$
   \\text{Final Score} = \\text{Actual Deviation} - \\text{Expected Tier Midpoint}
   $end:math:display$

   This final score reflects how far each department is from where we think they *should* be — helping us flag meaningful misalignments.

### 🎯 Why It Matters

This approach doesn’t just highlight high or low spenders — it shows where departments are behaving *differently than expected*, based on policy and context.  
The result is a heatmap that directs attention to areas of potential concern, waste, or policy drift — helping prioritize where to investigate next.

---

🧾 Sales Department – Office Supplies Deep Dive

This section focuses on how the Sales department spends on Office Supplies, breaking down patterns by employee, vendor, and time.

Using a custom analysis workflow, we:
	•	Identify employees or vendors with unusually high spending using z-score thresholds
	•	Track monthly spending trends to spot seasonal spikes or irregular activity
	•	Flag any purchases made on weekends or U.S. holidays
	•	Visualize spending concentration by employee and vendor
	•	Highlight transaction-level outliers to uncover red flags

This approach helps surface potential fairness issues, policy concerns, or unusual patterns that wouldn’t be obvious from totals alone.

---






## 🔍 Project Summary

- **Department Focus**: Sales  
- **Category Analyzed**: Office Supplies  
- **Dataset**: Internal transactions with columns `date`, `id`, `employee`, `vendor`, `amount`, `category`, `department`  
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

## 📋 Expense Policy Reference

To guide the analysis, the company follows clear policy rules for spending across categories:

| **Category**       | **Policy Rule**                                                                 |
|--------------------|----------------------------------------------------------------------------------|
| **Travel**         | Max **$855** per day per employee for travel-related expenses                   |
| **Meals**          | Max **$55** per meal per employee                                               |
| **Office Supplies**| Any transaction over **$650** requires manager approval                         |
| **Training**       | Max **$1,400** per employee per training/course                                 |
| **Software**       | Any new software purchase over **$2,000** must be procurement-approved          |

These benchmarks informed the policy-checking script and supported root-cause analysis for flagged outliers.

---

## 📂 Repository Structure

project-folder/
│
├── scripts/
│   └── 01_sales_office_supplies_analysis.py        # Full analysis script
│
├── data/
│   └── SmallCompany.csv                   # Cleaned expense data
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

## 🎥 Loom Video 

[Watch the walk-through →](https://loom.com/your-link-here)

---

## ✍️ Author

**Bryan H.**  
Aspiring Data Analyst focused on business intelligence, expense optimization, and operational insight.




  














   






   














  














   






   
