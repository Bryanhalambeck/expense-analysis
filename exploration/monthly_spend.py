# ============================================================
# 📊 monthly_spend.py
# ------------------------------------------------------------

import duckdb
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1️⃣ Load and Prepare Expense Data
# ------------------------------------------------------------
df = pd.read_csv("Untitledspreadsheet72.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Ensure datetime format

# ------------------------------------------------------------
# 2️⃣ Register DuckDB Table
# ------------------------------------------------------------
con = duckdb.connect()
con.register("expenses", df)

# ------------------------------------------------------------
# 3️⃣ Query: Monthly Total Spend
# ------------------------------------------------------------
monthly_trend = con.execute("""
    SELECT 
        DATE_TRUNC('month', date) AS month,
        SUM(amount) AS total_spend
    FROM expenses
    GROUP BY month
    ORDER BY month;
""").df()

# ------------------------------------------------------------
# 4️⃣ Clean and Format for Plotting
# ------------------------------------------------------------
monthly_trend['month'] = pd.to_datetime(monthly_trend['month'])

# ------------------------------------------------------------
# 5️⃣ Plot: Company-Wide Monthly Spend
# ------------------------------------------------------------
plt.figure(figsize=(10, 5))
plt.plot(monthly_trend['month'], monthly_trend['total_spend'], marker='o')
plt.title("📊 Company-Wide Monthly Spend (All Departments)")
plt.xlabel("Month")
plt.ylabel("Total Spend ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
