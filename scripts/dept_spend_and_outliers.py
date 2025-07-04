# ============================================
# 📊 02_dept_spend_and_outliers.py
# ============================================

import pandas as pd
import duckdb
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------
# 1️⃣ Load data
# --------------------------------------------
df = pd.read_csv("expenses23.csv")

# --------------------------------------------
# 2️⃣ Add transaction-level z-score
# --------------------------------------------
df['z_score'] = zscore(df['amount'])

# Register with DuckDB
con = duckdb.connect()
con.register('df', df)

# --------------------------------------------
# 3️⃣ Aggregate spend & outlier % per department
# --------------------------------------------
result = con.execute("""
    SELECT
        department,
        SUM(amount) AS total_spend,
        AVG(amount) AS avg_spend_per_expense,
        SUM(CASE WHEN ABS(z_score) > 1.5 THEN 1 ELSE 0 END) * 1.0 / COUNT(*) * 100 AS outlier_pct
    FROM df
    GROUP BY department
""").df()

# --------------------------------------------
# 4️⃣ Add Z-Scores
# --------------------------------------------
result['z_total_spend'] = zscore(result['total_spend']).round(2)
result['z_avg_spend'] = zscore(result['avg_spend_per_expense']).round(2)
result['z_outlier_pct'] = zscore(result['outlier_pct']).round(2)

# --------------------------------------------
# 5️⃣ Heatmap: Department Z-Scores
# --------------------------------------------
heatmap_data = result.set_index('department')[
    ['z_total_spend', 'z_avg_spend', 'z_outlier_pct']
]

plt.figure(figsize=(8, 5))
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", center=0)
plt.title("Department Z-Scores: Total Spend, Avg Spend, Outlier %")
plt.tight_layout()
plt.show()
