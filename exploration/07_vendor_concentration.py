# ============================================================
# 📊 vendor_concentration.py
# ------------------------------------------------------------
"""
Analyzes how much spend flows to each vendor, flags over reliance and identifies single-use vendors.
"""

import pandas as pd
import duckdb
from scipy.stats import zscore

# ------------------------------------------------------------
# 1️⃣ Load and Clean Data
# ------------------------------------------------------------
df = pd.read_csv("data/SmallCompany.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['vendor'] = df['vendor'].fillna("Unknown")

# ------------------------------------------------------------
# 2️⃣ Register Data with DuckDB
# ------------------------------------------------------------
con = duckdb.connect()
con.register("expenses", df)

# ------------------------------------------------------------
# 3️⃣ Aggregate Vendor Spend and Transaction Count
# ------------------------------------------------------------
vendor_summary = con.execute("""
    SELECT 
        vendor,
        SUM(amount) AS total_spend,
        COUNT(*) AS txn_count
    FROM expenses
    GROUP BY vendor
    ORDER BY total_spend DESC
""").df()

# ------------------------------------------------------------
# 4️⃣ Add Percent of Total and Z-Score
# ------------------------------------------------------------
vendor_summary['percent_of_total'] = vendor_summary['total_spend'] / vendor_summary['total_spend'].sum() * 100
vendor_summary['z_score'] = zscore(vendor_summary['total_spend'])

# ------------------------------------------------------------
# 5️⃣ Flag Vendor Risk Patterns
# ------------------------------------------------------------
def flag_vendor(row):
    if row['percent_of_total'] >= 30:
        return 'Hard High'
    elif row['z_score'] > 1.96:
        return 'Z Outlier'
    elif row['txn_count'] == 1:
        return 'Single-Use Vendor'
    else:
        return 'OK'

vendor_summary['Flag'] = vendor_summary.apply(flag_vendor, axis=1)
vendor_summary['percent_of_total'] = vendor_summary['percent_of_total'].round(2)

# ------------------------------------------------------------
# 6️⃣ Display Results
# ------------------------------------------------------------
print("🏪 Vendor Concentration Check — Company-Wide")
print(vendor_summary[['vendor', 'total_spend', 'percent_of_total', 'z_score', 'txn_count', 'Flag']])
