# ============================================================
# 📊 same_day_vendor.py
# ------------------------------------------------------------
"""
Checks for cases where an employee made multiple purchases from the same vendor on the same day — which could signal batching, duplicates, or policy issues. 
"""

import pandas as pd
import duckdb

# ------------------------------------------------------------
# 1️⃣ Load Data
# ------------------------------------------------------------
df = pd.read_csv("data/SmallCompany.csv")

# ------------------------------------------------------------
# 2️⃣ Register Cleaned Data with DuckDB
# ------------------------------------------------------------
con = duckdb.connect()
con.register("expenses", df)

# ------------------------------------------------------------
# 3️⃣ Query: Same-Day Vendor Transactions by Employee
# ------------------------------------------------------------
repeat_vendor_day = con.execute("""
    SELECT 
        employee,
        vendor,
        date,
        COUNT(*) AS txn_count,
        SUM(amount) AS total_amount
    FROM expenses
    GROUP BY employee, vendor, date
    HAVING COUNT(*) > 1
    ORDER BY txn_count DESC, total_amount DESC
""").df()

# ------------------------------------------------------------
# 4️⃣ Display Results
# ------------------------------------------------------------
print("🔁 Same-Day Vendor Usage by Employee:")
print(repeat_vendor_day)
