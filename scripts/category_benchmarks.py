# ============================================
# 📊 category_benchmarks.py
# --------------------------------------------
"""
This script analyzes departmental spending by category,
calculates deviation from benchmark expectations using 
custom tier midpoints, and visualizes the results in a heatmap.

📘 How it works:
- First, we calculate how much of each department's budget is spent on categories like Meals, Travel, etc.
- Then, we compare that to what's typical for each category across all departments.
- We also define what each department *should* be spending (e.g. low, medium-low, medium, medium-high, high).
- Finally, we check how far off each department is from that expectation — and show the results in a color-coded chart.

This helps spot over/under-spending behavior, highlight misalignments, and guide budget decisions across teams.

"""

import os
import pandas as pd
import duckdb
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_benchmark_heatmap(pivot_table, output_path):
    """Generate and save a heatmap of deviations from expected benchmarks."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, cmap="coolwarm", center=0, fmt=".1f")
    plt.title("Deviation from Expected Benchmark by Category Tier")
    plt.ylabel("Department")
    plt.xlabel("Category")
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":

    # -----------------------------
    # 1️⃣ Load Data
    # -----------------------------
    df = pd.read_csv("data/SmallCompany.csv")

    # -----------------------------
    # 2️⃣ % of Department Spend by Category
    # -----------------------------
    df_dept_cat = duckdb.query("""
        WITH dept_totals AS (
            SELECT department, SUM(amount) AS dept_total
            FROM df
            GROUP BY department
        ),
        category_spend AS (
            SELECT department, category, SUM(amount) AS category_total
            FROM df
            GROUP BY department, category
        )
        SELECT
            cs.department,
            cs.category,
            ROUND(100.0 * cs.category_total / dt.dept_total, 2) AS percent_of_dept_spend
        FROM category_spend cs
        JOIN dept_totals dt
        ON cs.department = dt.department
    """).df()

    # -----------------------------
    # 3️⃣ Deviation from Category Average
    # -----------------------------
    category_avg = df_dept_cat.groupby('category')['percent_of_dept_spend'].mean().round(2)
    df_dept_cat['deviation_from_avg'] = df_dept_cat['percent_of_dept_spend'] - df_dept_cat['category'].map(category_avg)

    pivot_dev = df_dept_cat.pivot(index='department', columns='category', values='deviation_from_avg').fillna(0)

    # -----------------------------
    # 4️⃣ Define Benchmark Tier Midpoints
    # -----------------------------
    deviation_values = pivot_dev.values.flatten()
    sorted_dev = np.sort(deviation_values[~np.isnan(deviation_values)])

    low_cutoff = np.percentile(sorted_dev, 33)
    high_cutoff = np.percentile(sorted_dev, 66)

    low_mid = np.mean(sorted_dev[sorted_dev < low_cutoff])
    med_mid = np.mean(sorted_dev[(sorted_dev >= low_cutoff) & (sorted_dev <= high_cutoff)])
    high_mid = np.mean(sorted_dev[sorted_dev > high_cutoff])
    med_low_mid = (low_mid + med_mid) / 2
    med_high_mid = (med_mid + high_mid) / 2

    # -----------------------------
    # 5️⃣ Manual Expected Tiers
    # -----------------------------
    expected_tiers = {
        ('Engineering', 'Meals'): 'Low',
        ('Engineering', 'Office Supplies'): 'Medium–Low',
        ('Engineering', 'Software'): 'High',
        ('Engineering', 'Training'): 'Medium–High',
        ('Engineering', 'Travel'): 'Low',

        ('Marketing', 'Meals'): 'High',
        ('Marketing', 'Office Supplies'): 'Medium',
        ('Marketing', 'Software'): 'Medium–High',
        ('Marketing', 'Training'): 'Medium',
        ('Marketing', 'Travel'): 'High',

        ('Sales', 'Meals'): 'High',
        ('Sales', 'Office Supplies'): 'Low',
        ('Sales', 'Software'): 'Medium–High',
        ('Sales', 'Training'): 'Medium–High',
        ('Sales', 'Travel'): 'High',

        ('HR', 'Meals'): 'Medium',
        ('HR', 'Office Supplies'): 'Medium',
        ('HR', 'Software'): 'Low',
        ('HR', 'Training'): 'High',
        ('HR', 'Travel'): 'Medium',

        ('IT', 'Meals'): 'Low',
        ('IT', 'Office Supplies'): 'Medium',
        ('IT', 'Software'): 'High',
        ('IT', 'Training'): 'High',
        ('IT', 'Travel'): 'Low',
    }

    # -----------------------------
    # 6️⃣ Compare Actual vs Expected
    # -----------------------------
    comparison = []
    for dept in pivot_dev.index:
        for cat in pivot_dev.columns:
            actual_dev = pivot_dev.loc[dept, cat]
            tier = expected_tiers.get((dept, cat), 'Medium')
            benchmark = {
                'Low': low_mid,
                'Medium–Low': med_low_mid,
                'Medium': med_mid,
                'Medium–High': med_high_mid,
                'High': high_mid
            }[tier]
            comparison.append((dept, cat, round(actual_dev - benchmark, 2)))

    df_comp = pd.DataFrame(comparison, columns=['department', 'category', 'dev_from_expected'])
    pivot_expected = df_comp.pivot(index='department', columns='category', values='dev_from_expected')

    # -----------------------------
    # 7️⃣ Heatmap of Deviation from Expected Benchmark
    # -----------------------------
    generate_benchmark_heatmap(pivot_expected, "charts/benchmark_heatmap.png")
