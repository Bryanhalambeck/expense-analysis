# ============================================================
# 📊 same_day_vendor.py
# ------------------------------------------------------------
"""
This script checks for vendor concentration risk by analyzing how much of the company’s total spend is flowing to each vendor — and flags cases that may warrant scrutiny.

📘 How it works:
	•	We calculate total spend and number of transactions for each vendor.
	•	Then, we compute:
	•	Percent of total spend (to flag overly dominant vendors)
	•	Z-score (to identify statistical outliers)
	•	Single-use vendors (which may indicate inconsistent procurement practices)
	•	Vendors are flagged as:
	•	🔴 Hard High: 30%+ of total spend
	•	⚠️ Z Outlier: Statistically unusual spending (z > 1.96)
	•	🟡 Single-Use Vendor: Only one transaction
	•	✅ OK: No immediate red flag

This analysis helps detect overreliance, potential risk exposure, and opportunities for vendor consolidation.
import duckdb
"""

# ------------------------------------------------------------
# 1️⃣ Register Cleaned Data with DuckDB
# ------------------------------------------------------------
con = duckdb.connect()
con.register("expenses", df)  # Assumes `df` is already loaded

# ------------------------------------------------------------
# 2️⃣ Query: Same-Day Vendor Transactions by Employee
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
# 3️⃣ Display Results
# ------------------------------------------------------------
print("🔁 Same-Day Vendor Usage by Employee:")
print(repeat_vendor_day)
