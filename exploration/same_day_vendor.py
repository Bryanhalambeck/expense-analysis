# ============================================================
# 📊 same_day_vendor.py
# ------------------------------------------------------------
"""
This script flags repeat transactions with the same vendor on the same day by a single employee — which can signal batching, duplicate purchases, or policy issues.

📘 How it works:
	•	We group expenses by employee, vendor, and date.
	•	Any combination with more than one transaction on the same day is flagged.
	•	For each match, we show the number of transactions and total amount spent.

This check helps spot possible oversights, double charges, or non-standard purchasing behavior — useful for tightening vendor and employee-level controls.
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
