## 📊 Expense Insights & Risk Detection for a Small Tech & Professional Services Firm 

---

## 📌 Executive Summary

This project analyzes expense data for a small tech and professional services firm to uncover fairness concerns, policy violations, vendor risks, and unusual spending patterns.  

It delivers two fully finalized analyses:  
- **📊 Company-Wide Category Benchmarking** – A cross-department comparison showing where spending in department–category pairs falls above or below expected levels, visualized in a custom benchmark heatmap.  
- **🧾 Detailed Analysis: Sales – Office Supplies** – A breakdown of one flagged department–category pair, including z-score outlier detection for employees and vendors, timing checks, vendor concentration analysis, and transaction-level anomaly detection.  

These two analyses are complete, visualized, and explained in the README, showing the end-to-end workflow from raw data to actionable insight.  

The `/exploration/` folder contains additional scripts that extend this risk-detection approach to the entire company. These are not finalized into README visuals or write-ups, but they demonstrate how the project could scale to a full-company audit — applying the same investigative principles through other methods.

In short, the finalized pieces show **how a full, polished analysis looks**, while the exploratory scripts show **how the process could be expanded across all departments and categories**.

---

### 👤 Example Company Description  
The company is a small, specialized tech and professional services firm run by a lean team of six core employees. This tight-knit group handles custom software development, IT support, marketing campaigns, sales operations, and HR tasks for a range of clients across industries.  

Because the company is small and agile, each employee wears multiple hats — working across departments to manage different projects, budgets, and client needs. As a result, all six employees are expected to share spending responsibilities equally — meaning their expenses should generally be balanced across departments and categories.  

The organization maintains clear expense policies to keep spending in check while balancing remote and in-office work, plus regular travel for client meetings, conferences, and training.  

---

### 💼 Project Brief: Expense Analysis for Finance 

You’re our sole data analyst, and we need your help reviewing last year’s company expense records to spot early red flags, potential policy violations, or cost-saving opportunities. We’ve provided you with a raw expense file containing details like date, department, category, employee, vendor, and amount — all tied back to the same six employees who spend across every department.

While this dataset covers our entire operation, we need you to focus on delivering actionable findings within a short turnaround to help guide our upcoming budget discussions. Given the time constraints, we’re not expecting a detailed analysis into every department–category pair. Instead, apply your detailed analysis methods to the highest-priority cases.

Your goal is to turn this data into clear, actionable insights that will help us spend wisely, stay within budget as we grow, and flag any spending patterns that look significantly above or below the fair share expected for each employee.

---

### 📋 Example Company's Expense Policy Reference

| **Category**        | **Policy Rule**                                                                 |
|---------------------|----------------------------------------------------------------------------------|
| **Travel**          | Max **$855** per day per employee                                               |
| **Meals**           | Max **$55** per meal per employee                                               |
| **Office Supplies** | Any transaction over **$650** requires approval                                 |
| **Training**        | Max **$1,400** per employee per training/course                                 |
| **Software**        | Any new software purchase over **$2,000** must be procurement-approved          |

---

### 📁 Data Source – `SmallCompany.csv`

This file contains 100 rows of fictional expense data from the small tech and services firm. Each row represents an individual transaction made by one of six core employees across various departments and categories.

#### 🔍 Columns:
- **id** – Unique transaction ID  
- **date** – Purchase date (`MM/DD/YY` format)  
- **department** – Department responsible for the spend (e.g., Sales, IT, Marketing)  
- **vendor** – The company or service where the expense occurred  
- **employee** – The individual who made the purchase  
- **category** – Type of expense (e.g., Travel, Software, Office Supplies)  
- **amount** – Transaction amount in USD  

#### 🧾 Purpose:
This file serves as the base dataset for all analysis in this project. It was designed to mimic realistic company spending behavior, including:

- Overlapping responsibilities across employees and departments  
- Diverse vendor usage  
- A variety of expense types

---

### 📊 Category-Level Benchmarking (All Departments)

This analysis compares each department’s spending behavior to what’s expected across categories (Travel, Meals, Office Supplies, Training, Sales), then visualizes differences in a heatmap.

**At a glance:** 
- Calculates what % of each department’s budget goes to each category  
- Compares that to what’s typical across all departments  
- Defines expected spend levels (Low, Medium-Low, Medium, Medium-High, High) for each department and category  
- Visualizes how far off each department is from those expectations using a color-coded heatmap

---

<details>
  <summary><strong>✅ Step-by-Step Benchmarking Process (click to expand)</strong></summary>

1. **% of Department Spend by Category**  
Percent = (Category Spend / Total Dept Spend) × 100  
→ This gives a normalized view of each department’s spending priorities.

2. **Deviation from Category Average**  
Deviation = (This Dept’s % Spend) – (Category Average % Spend)  
→ This tells us how unusually high or low a department is spending in each area.

3. **Tier Midpoints from Percentiles**  
I split all deviation values into percentile-based tiers:  
- Bottom 33% → Low  
- Middle 33% → Medium  
- Top 33% → High  

In-between midpoints:  
- Medium–Low = average of Low and Medium  
- Medium–High = average of Medium and High  

4. **Manual Tier Expectations**  
Based on business context, I manually defined expected tier behavior for each department/category pair.  
📝 *Note: Full tier assignments are available in the code for transparency. These were based on common sense assumptions for a small team with shared spending responsibilities.*

5. **Deviation from Expected Benchmark**  
Final Score = Actual Deviation – Expected Tier Midpoint  
→ This reflects how far each department is from where they should be. 

</details>

---

### 🎯 Why It Matters

This approach doesn’t just highlight high or low spenders — it shows where departments are behaving differently than expected.

The resulting heatmap offers:

- ✅ Targeted Diagnosis: Flag potential problem areas  
- 📊 Executive Overview: Give leadership a clean snapshot of department behavior

---

### 🧾 Detailed Analysis: Sales – Office Supplies  

This analysis examines the Sales department’s Office Supplies spending by employee, vendor, timing, and transaction detail to uncover patterns and potential red flags not visible from totals alone.  

**At a glance:** 
- Flags employees or vendors with unusually high spend using z-scores  
- Tracks monthly spend trends to spot spikes or seasonal patterns  
- Detects purchases on weekends or U.S. holidays  
- Visualizes spending concentration by employee, vendor, and transaction  
- Highlights outliers for deeper investigation  

---

<details>
  <summary><strong>✅ Step-by-Step Analysis Workflow (click to expand)</strong>
  </summary>


1. **Targeted Subset**  
Focus only on Sales department’s Office Supplies transactions.

2. **Employee-Level Analysis**  
Sum each employee’s spend in this category.  
→ Flag z-scores > 1.0 to catch above-average behavior.

3. **Vendor-Level Analysis**  
Sum each vendor’s spend in this category.  
→ Flag z-scores > 1.5 to catch overreliance.

4. **Monthly Spend Trends**  
Group spending by month to detect seasonal or unusual spikes.

5. **Transaction-Level Outliers**  
Calculate z-scores for each individual transaction.  
→ Flag z > 1.5 to catch standout anomalies.  
📝 *Note: Z-score thresholds vary slightly to avoid false positives.*

6. **Timing Flags**  
Flag any purchases made on weekends or U.S. holidays.

7. **Employee Spend Share**  
Calculate each employee’s percentage of the total category spend.  
→ Compare against an equal-share benchmark (**~16.7%**) to identify imbalances.

8. **Vendor Breakdown Pie Chart**  
Visualize vendor concentration.

10. **Transaction Strip Plot**  
Show every transaction by employee to spot extremes or clusters.

</details>

---

### 🎯 Why It Matters

This department-level workflow enables the finance team to:

- ✅ Flag fairness concerns in how spending is distributed  
- ✅ Spot vendor overuse or unusual purchase timing  
- ✅ Identify transactions that significantly impact total spend

This supports smarter audits, tighter controls, and cleaner, more transparent budgets.

---

### 📊 Final Visuals and Insights

![Sales Employee Share Z-Score](charts/employee_spend.png)  
📎 **David Kim and Frank Wu were both flagged as outliers** in the Sales department’s Office Supplies spending based on z-scores.

This bar chart compares each employee’s share of total Office Supplies spending within the Sales department.  
The red dashed line represents the expected even share if spending were split equally among all employees (~16.7%).

- 🟠 **David Kim** had a z-score > **+1.0**, marking him as a high-end outlier 
- 🟠 **Frank Wu** had a z-score < **-1.0**, marking him as a low-end outlier  
- 🔵 Blue bars indicate spending within the normal range
- 🟠 Orange bars mark employees whose spending was flagged as an outlier (z-score > 1.0 or < -1.0)

This view helps surface fairness issues and possible budget misuse that wouldn’t be clear from totals alone.

---

![Vendor Breakdown Pie Chart](charts/vendor_breakdown.png)  

📎 **Over 60% of all Office Supplies purchases in Sales went to Staples** — flagged as a potential outlier based on vendor z-score.

This pie chart breaks down which vendors received Office Supplies spending from the Sales department:

- 🏪 Staples received a dominant 60.6% share, exceeding the 1.5 z-score threshold and suggesting possible overreliance.
- 📦 Amazon and Office Depot split most of the remaining spend in more typical proportions.
- ❓ Hilton received 4.4% of spend — an unusual vendor for Office Supplies.

This visualization helps highlight potential overreliance on specific vendors and raises questions about purchasing diversity or policy alignment.

---

![Transaction Outlier Chart](charts/transactions.png)  
📎 **A single $972 transaction by David Kim** stands out at over +2 standard deviations above the mean — flagged as a potential red flag based on z-score.

This chart shows all individual Office Supplies transactions in the Sales department, plotted by employee.

- 🔘 Gray dots represent standard transactions  
- 🔴 Red dot marks a transaction flagged as an outlier (z > 1.5)  
- 🔵 Blue dashed lines show the mean and standard deviation thresholds
- 🔴 **David Kim** had a z-score > **+1.5**, marking him as a high-end outlier 

This view helps uncover isolated spikes in spending that wouldn’t be caught through total summaries — offering a clear lens on potential misuse or exception-based activity.

---

![Category Benchmark Heatmap](charts/category_tiers.png)  
📎 **This heatmap shows how far each department’s category-level spend deviates from its expected benchmark** — highlighting major over- or under-spending areas.

Each cell represents a department’s deviation (in percentage points) from its expected category spending tier.

- 🔴 Red cells indicate spending **above** expected levels  
- 🔵 Blue cells indicate spending **below** expectations  
- 🔘 Neutral colors show spending **in line** with expectations

For example:

- **Sales** spent **28.3 percentage points more** on Office Supplies than expected  
- **Engineering** spent **22 points less** than expected on Software

This visual quickly surfaces policy misalignment, budget anomalies, or misprioritized resources that would be missed in raw totals or standard breakdowns.

---

## 📌 Final Report & Recommendations – Sales Department: Office Supplies

### Key Insights
- **Employee Spending Outliers:** David Kim and Frank Wu were flagged as significant outliers based on z-scores.  
  - David Kim spent **well above** the expected share of team spending.  
  - Frank Wu spent **well below**, indicating an imbalance in resource usage.
- **Vendor Concentration Risk:** Over **60%** of category spend went to **Staples**, exceeding the 1.5 z-score threshold for vendor overreliance.  
- **Unusual Vendor Use:** Hilton accounted for **4.4%** of Office Supplies spend — atypical for this category and worth reviewing for coding or policy compliance issues.  
- **High-Value Transaction Alert:** A single **$972 purchase** by David Kim was more than **+2 standard deviations above the mean**, exceeding the 1.5 z-score threshold for individual transactions.
- **Weekend & Holiday Purchases:**  
  - 2024-10-26: Alice Johnson spent **$426.27** at Office Depot (Weekend).  
  - 2024-12-25: Ella Martinez spent **$318.37** at Amazon (U.S. Holiday).  

### Business Implications
- **Fairness Concerns:** Imbalanced employee spending can create internal equity issues and suggests uneven budget access.  
- **Operational Risk:** Heavy reliance on one vendor reduces bargaining power and can disrupt supply if that vendor is unavailable.   
- **Timing Risk:** Weekend and holiday transactions may bypass normal oversight, increasing the chance of non-compliant or fraudulent purchases.  
- **Data Integrity:** Unusual vendor assignments (e.g., Hilton for Office Supplies) may signal misclassified expenses or potential misuse.

### Recommended Next Steps
1. **Outlier Review**
   - Audit the $972 transaction.
2. **Vendor Strategy**
   - Negotiate bulk purchase agreements with Staples to secure better pricing, or diversify suppliers to reduce dependency.
3. **Expense Classification Audit**
   - Review Hilton transaction to confirm if it was miscoded or genuinely related to Office Supplies.
4. **Timing Oversight**
   - Review weekend and holiday purchases for legitimacy and ensure proper approval processes are followed.
5. **Ongoing Monitoring**
   - Implement automated alerts for:
     - Vendors receiving >50% of spend in any category.
     - Employee spending exceeding +1.0 z-score in a given category.
     - Vendor spending exceeding +1.5 z-score in a given category.
     - Individual transactions exceeding +1.5 z-score in a given category.
     - Purchases made on weekends or recognized holidays.

---

### 🧪 **Exploratory Scripts (Not Finalized)**  

In addition to the two finalized outputs, I built and tested a range of company-wide supporting tools that reflect my full analytical process.  

While most of these were coded and tested in /exploration/, one item — the Vendor–Category Mismatch Check — was identified as a useful future enhancement but was not implemented as a working script for this version of the project. It’s included here for completeness, as it would strengthen coverage in a full audit scenario.

These exploratory scripts were not fully polished into final charts or visuals in the README, nor were they fully developed and documented like the finalized category heatmap and Sales Office Supplies analysis. However, they reflect the complete analytical workflow I would follow to scale this project — providing clear examples of how I would extend the process across all departments and any category flagged for review.   

- 🚨 **Policy Violation Check**  
  Scans all transactions across the company and flags any that exceed category-specific spending limits.  

- 🧾 **Company-Wide Vendor Risk Analysis**  
  Analyzes how much spend flows to each vendor, flags over reliance and identifies single-use vendors.
  
-	🏷 **Vendor–Category Mismatch Check (planned)**  
  Scans for unusual vendor–category pairings (e.g., a hotel coded under Office Supplies), helping flag possible misclassifications or policy compliance issues that may not appear in high-level budget deviation checks.

- 🔁 **Same-Day Vendor Repeats**  
  Checks for cases where an employee made multiple purchases from the same vendor on the same day — which could signal batching, duplicates, or policy issues.  

- 📈 **Monthly Spend Trends**  
  Groups total company expenses by month to visualize spending cycles, spot seasonal spikes, or highlight unusual surges.  

- 🔍 **Sales Department Category Scan**  
  Provides a quick summary of how the Sales team spent across all categories except Office Supplies (which was covered in a full detailed analysis). Flags all timing issues and outliers.

These scripts helped me cover the full scope of my assigned goal and ensured I could identify issues across departments.

📁 See all supporting analysis in /exploration/

---

### 📌 **What I’d Do If This Were a Full Audit**  

If I were continuing this analysis as part of a full audit, I would:  
- ✅ Conduct full, detailed analyses — like the Sales–Office Supplies example — for every department-category combination in the heatmap that shows a deviation large enough to warrant deeper investigation (e.g. +20% or –15% or more from benchmark expectations). 
- ✅ Create brief department overviews for each team (like I did for Sales) to summarize spending behavior across categories.  
- ✅ Finalize each company-wide script by converting it into a clear visual summary and polished, executive-ready output.
- ✅ Run a company-wide vendor–category mismatch audit to catch unusual pairings (e.g., a hotel vendor appearing in Office Supplies), helping flag possible misclassifications or policy compliance issues that may not appear in high-level budget deviation checks.

---

### 🔍 **Project Summary**

- **Company-Wide Category Benchmarking** 
- **Detailed Analysis: Sales – Office Supplies**

- **Company-Wide Explorations** *(in `/exploration/`)*:  
  - Policy violation checks  
  - Vendor concentration & single-use vendor identification
  - (Planned) Vendor–category mismatch check 
  - Same-day vendor repeat detection  
  - Monthly spending trend visualization  
  - Sales department category scan (non–Office Supplies)  

- **Dataset:** Internal transactions including:  
  `date`, `department`, `category`, `employee`, `vendor`, `amount`  

- **Tools & Methods:**  
  Python • Pandas • DuckDB • Seaborn • Matplotlib • Z-score analysis • Custom category benchmarking

---

### 📂 Repository Structure
```plaintext
project-folder/
│
├── charts/
│   ├── employee_spend.png
│   ├── vendor_breakdown.png
│   ├── transactions.png
│   └── category_tiers.png
│
├── data/
│   └── SmallCompany.csv
│
├── exploration/
│   ├── monthly_spend.py
│   ├── policy_checks.py
│   ├── sales_check.py
│   ├── same_day_vendor.py
│   └── vendor_concentration.py
│
├── scripts/
│   ├── category_benchmarks.py
│   └── sales_office_supplies.py
│
├── requirements.txt
└── README.md
```

---

### 🧠 **Skills Demonstrated**

- Real-world anomaly detection using **z-scores**  
- Building **custom business benchmarking** logic for category comparisons  
- Filtering, grouping, and aggregating transaction data for insight discovery  
- **Visual storytelling** through clear, actionable charts  
- Using **DuckDB in Python** for fast, SQL-style querying  
- Communicating findings in a **clear, structured, and business-friendly** format

---

### 🎥 **Loom Video**  
Watch the walk-through → [https://loom.com/your-link-here](https://loom.com/your-link-here)  

---

### ✍️ **Author**  
**Bryan H.**  
Aspiring Data Analyst focused on business intelligence, expense optimization, and operational insight.  
