# expense-analysis

## Example Company Description

The company is a small, specialized tech and professional services firm run by a lean team of six core employees. This tight-knit group handles custom software development, IT support, marketing campaigns, sales operations, and HR tasks for a range of clients across industries.

Because the company is small and agile, each employee wears multiple hats — working across departments to manage different projects, budgets, and client needs. As a result, all six employees are expected to share spending responsibilities equally — meaning their expenses should generally be balanced across departments and categories.

The organization maintains clear expense policies to keep spending in check while balancing remote and in-office work, plus regular travel for client meetings, conferences, and training.

---

💼 Business Scenario: Expense Review for Finance

You’re the sole data analyst supporting this small team. The finance lead has asked you to analyze the company’s expense records from the past year to spot early red flags, policy violations, or cost-saving opportunities.

You’ve been given a raw expense file that includes details like date, department, category, employee, vendor, and amount — all linked back to the same six employees who spend across every department.

Your goal is to turn this data into clear, actionable insights that help the team spend wisely and stick to budget as they grow — while flagging any spending patterns that look significantly above or below the fair share expected for each employee.

---

📁 Data Source – SmallCompany.csv

This file contains 100 rows of fictional expense data from the small, specialized tech and professional services firm. Each row represents an individual transaction made by one of six core employees across various departments and categories.

🔍 Columns:
	•	id – Unique transaction ID
	•	date – Purchase date (MM/DD/YY format)
	•	department – Department responsible for the spend (e.g., Sales, IT, Marketing)
	•	vendor – The company or service where the expense occurred
	•	employee – The individual who made the purchase
	•	category – Type of expense (e.g., Travel, Software, Office Supplies)
	•	amount – Transaction amount in USD

🧾 Purpose:

This file serves as the raw input for all analysis in this project. It was designed to mimic realistic company spending behavior, including:
	•	Overlapping responsibilities across employees and departments
	•	Diverse vendor usage
	•	A variety of expense types
	
---

# 📊 Category-Level Benchmarking (All Departments)

This section evaluates how each department’s spending behavior aligns with expectations across categories like Travel, Meals, Office Supplies, Training and Travel.

Using a custom benchmarking system, we:
- Calculate what % of each department's budget went to each category
- Compare that to what’s typical across departments
- Define “expected” spending tiers (low, medium-low, medium, medium-high, high) for each category
- Visualize how far off each department is from those expectations using a color-coded heatmap

This approach flags misalignments and potential budget issues that wouldn’t show up in raw totals alone.

---

## 📊 Benchmarking Logic Explained

To help identify which department-category pairs might warrant deeper investigation, I built a custom benchmarking system. This system scores each department based on how closely its spending aligns with expectations.

Here’s how it works:

### ✅ Step-by-Step Logic

1. **% of Department Spend by Category**  
   For each department, I calculated the percentage of their total budget spent in each category (Meals, Travel, etc.):

   Percent = (Category Spend / Total Dept Spend) × 100

   This gives a normalized view of each department’s spending priorities.

2. **Deviation from Category Average**  
   I then subtracted the company-wide average for each category:

   Deviation = (This Dept’s % Spend) – (Category Average % Spend)

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
   I manually defined what tier each department should be in for each category, based on the business context, and general expectations for how resources are typically allocated in a small, shared-spending team. 
   (e.g., Sales is expected to spend “Low” on Office Supplies, “High” on Travel.)

5. **Deviation from Expected Benchmark**  
   I then compared each department’s actual deviation to its expected tier midpoint:

   Final Score = Actual Deviation – Expected Tier Midpoint

   This final score reflects how far each department is from where we think they *should* be — helping us flag meaningful misalignments.

### 🎯 Why It Matters

This approach doesn’t just highlight high or low spenders — it shows where departments are behaving differently than expected, based on policy and context.

The resulting heatmap serves two key purposes:
	•	✅ Targeted Diagnosis: It flags potential problem areas — like overspending or policy misalignment — helping the finance team know exactly where to dig in.
	•	📊 Executive Overview: It gives leadership a clean, visual snapshot of how each department stacks up across all categories — making it easier to spot outliers, patterns, or blind spots at a glance.

Whether you’re looking for a specific red flag or zooming out for strategic decision-making, this benchmarking system helps translate raw numbers into actionable insights.

---

🧾 Sales Department – Office Supplies Deep Dive

This section focuses on how the Sales department spends on Office Supplies, breaking down patterns by employee, vendor, individual transactions and time.

Using a custom analysis workflow, we:
	•	Identify employees or vendors with unusually high spending using z-score thresholds
	•	Track monthly spending trends to spot seasonal spikes or irregular activity
	•	Flag any purchases made on weekends or U.S. holidays
	•	Visualize spending concentration by employee, individual transaction and vendor
	•	Highlight transaction-level outliers to uncover red flags

This approach helps surface potential fairness issues, policy concerns, or unusual patterns that wouldn’t be obvious from totals alone.

---

🧾 Office Supplies Logic Explained

This analysis takes a focused look at Office Supplies spending within the Sales department, using z-score thresholds and visual breakdowns to identify potential red flags — whether it’s an overactive employee, a concentrated vendor, an oddly timed purchase, or a standout one-off transaction.

✅ Step-by-Step Logic
    1.    Targeted Subset
We isolate just the Sales department’s Office Supplies transactions, zeroing in on one department-category combo for focused analysis.
    2.    Employee-Level Analysis
We sum each employee’s total Office Supplies spend, then apply a z-score to flag outliers.
    •    Employees with z > 1.0 are highlighted as potentially overspending compared to peers.
    3.    Vendor-Level Analysis
We repeat the same logic for vendors.
    •    Vendors with z > 1.5 are flagged to check for overreliance or unusual billing.
    4.    Monthly Spend Trends
Spending is grouped by month to visualize spikes or trends over time — helping identify seasonality or sudden jumps.
    5.    Transaction-Level Outliers
We calculate a z-score for each individual transaction, flagging any with z > 1.5 as potentially anomalous.
  Note: Different z-score thresholds (e.g., 1.0 vs 1.5) are used based on the expected variation   in each area — helping surface meaningful outliers without over-flagging normal behavior.
    6.    Policy Checks (Weekends + Holidays)
Purchases on weekends or U.S. holidays are flagged, since these may violate company timing policies or require extra scrutiny.
    7.    Employee % Share Bar Chart
A horizontal bar chart shows how much each employee contributed to total spend, compared to an even split.
  •  Bars with a z-score greater than 1.0 are visually flagged in orange to highlight potential outliers.
    8.    Vendor Breakdown Pie Chart
A simple pie chart shows vendor share of total Office Supplies purchases — highlighting whether spend is spread or concentrated.
    9.    Transaction Strip Plot
A final strip plot charts all transactions by employee, highlighting any that stand far above the norm — especially if it’s the same person repeatedly.

🎯 Why It Matters

By zooming in on one category and department, this analysis helps the finance team:
    •    Catch unusual spending behavior early
    •    Detect vendor dependence or policy violations
    •    Spot trends or exceptions that get buried in raw totals

This department-level deep dive supports smarter audits, tighter controls, and cleaner budgets.

---

## 📊 Final Visuals and Insights

![Sales Employee Share Z-Score](charts/employee_spend.png)  
📎 David Kim accounts for over 40% of total Office Supplies spend — flagged via z-score as a potential outlier, well above the expected average of ~16.7%.

This bar chart compares each employee’s share of total Office Supplies spending within the Sales department.
The red dashed line represents the expected even share if spending were split equally among all employees.
	•	Blue bars indicate within-normal-range spending.
	•	Orange bars mark employees whose spending was flagged as an outlier (z-score > 1.0 or < -1.0).

This view helps surface fairness issues and possible budget misuse that wouldn’t be clear from totals alone.

![Sales Employee Share Z-Score](charts/vendor_breakdown.png)  
📎 Over 60% of all Office Supplies purchases in Sales went to Staples, suggesting a heavy vendor concentration.

This pie chart breaks down which vendors received Office Supplies spending from the Sales department.
    •    A dominant share went to Staples (60.6%), while Amazon and Office Depot split most of the remaining spend.
    •    A smaller portion (4.4%) went to Hilton — an unusual entry for this category.

This visualization helps highlight potential overreliance on specific vendors and raises questions about purchasing diversity or policy alignment.


![Sales Employee Share Z-Score](charts/transaction_outlier.png)  
📎 A single $972 transaction by David Kim stands out at over +2 standard deviations above the mean — flagged as a potential red flag based on z-score.

This chart shows all individual Office Supplies transactions in the Sales department, plotted by employee.
    •    Gray dots represent standard transactions.
    •    The red dot marks a transaction flagged as an outlier (z > 1.5).
    •    Blue dashed lines show the mean and key standard deviation thresholds for context.

This view helps uncover isolated spikes in spending that wouldn’t be caught through total summaries — offering a clear lens on potential misuse or exception-based activity.

![Sales Employee Share Z-Score](charts/category_tiers.png)  
📎 This heatmap shows how far each department’s category-level spend deviates from its expected benchmark — highlighting major over- or under-spending areas.

Each cell represents a department’s deviation (in percentage points) from its expected category spending tier:
    •    🔴 Red cells indicate spending above expected levels.
    •    🔵 Blue cells indicate spending below expectations.
    •    ⚪ Neutral colors show spending roughly in line with expectations.

For example:
    •    Sales overspent on Office Supplies by +28.3 points compared to what was expected.
    •    Engineering underspent on Software by over 22 points.

This visual quickly surfaces policy misalignment, budget anomalies, or misprioritized resources that would be missed in raw totals or standard breakdowns.

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

- **Full Company Policy Check** (flag overspending by category across all departments)  
- **Same-Day Vendor Flagging** (detect duplicate or batched transactions from same employee/vendor)  
- **Full Vendor Benchmarking** (identify overreliance, statistical outliers, and single-use vendors)  
- **Departmental Timing Patterns** (analyze spending behavior by day, category gaps, and weekend use)  
- **Monthly Spend Trends** (visualize company-wide spending patterns over time to spot seasonal surges)  

Due to time constraints, I focused instead on building a strong, polished deep dive into the Sales department — but I’ve included my broader plan here to show my workflow, audit mindset, and ability to prioritize when scoping a real-world project.

👉 See additional scripts in `/exploration/` for experiments and early versions of broader analysis ideas.

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




  














   






   














  














   






   
