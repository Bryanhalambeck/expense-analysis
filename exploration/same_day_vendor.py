# ============================================================
# 📊 same_day_vendor.py
# ------------------------------------------------------------

import duckdb

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
