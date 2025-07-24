# =====================================================
# 📊 sales_check.py
# -----------------------------------------------------
# Analyzes Travel and Meals spending in the Sales dept,
# detecting outliers by employee, vendor, and weekend use.
# =====================================================

import pandas as pd
import duckdb
from scipy.stats import zscore

# -----------------------------------------------------
# 1️⃣ Load Data and Create Flags
# -----------------------------------------------------
df = pd.read_csv("Untitledspreadsheet72.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['day_of_week'] = df['date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'] >= 5

# -----------------------------------------------------
# 2️⃣ Register with DuckDB
# -----------------------------------------------------
con = duckdb.connect()
con.register("sales_data", df)

# -----------------------------------------------------
# 3️⃣ Travel Spend – Sales Department
# -----------------------------------------------------
sales_travel = con.execute("""
    SELECT * FROM sales_data
    WHERE department = 'Sales' AND category = 'Travel'
""").df()

# Employee-Level Travel Spend
employee_travel = sales_travel.groupby('employee')['amount'].sum().reset_index()
employee_travel['z_score'] = zscore(employee_travel['amount'])

print("✈️ Travel Spend by Employee (Sales Dept):")
print(employee_travel.sort_values('amount', ascending=False))

print("\n🚩 Employees with Travel z-score > 1.5:")
print(employee_travel[employee_travel['z_score'] > 1.5])
print("\n" + "="*50 + "\n")

# Vendor-Level Travel Spend
vendor_travel = sales_travel.groupby('vendor')['amount'].sum().reset_index()
vendor_travel['z_score'] = zscore(vendor_travel['amount'])

print("✈️ Travel Spend by Vendor (Sales Dept):")
print(vendor_travel.sort_values('amount', ascending=False))

print("\n🚩 Vendors with Travel z-score > 1.5:")
print(vendor_travel[vendor_travel['z_score'] > 1.5])
print("\n" + "="*50 + "\n")

# Weekend Travel Transactions
weekend_travel = sales_travel[sales_travel['is_weekend']]
print("📅 Weekend Travel Transactions (Sales Dept):")
print(weekend_travel[['date', 'employee', 'vendor', 'amount']])
print("\n" + "="*50 + "\n")

# -----------------------------------------------------
# 4️⃣ Meals Spend – Sales Department
# -----------------------------------------------------
sales_meals = con.execute("""
    SELECT * FROM sales_data
    WHERE department = 'Sales' AND category = 'Meals'
""").df()

# Employee-Level Meals Spend
employee_meals = sales_meals.groupby('employee')['amount'].sum().reset_index()
employee_meals['z_score'] = zscore(employee_meals['amount'])

print("🍽️ Meals Spend by Employee (Sales Dept):")
print(employee_meals.sort_values('amount', ascending=False))

print("\n🚩 Employees with Meals z-score > 1.0:")
print(employee_meals[employee_meals['z_score'] > 1.0])
print("\n" + "="*50 + "\n")

# Weekend Meals Transactions
weekend_meals = sales_meals[sales_meals['is_weekend']]
print("📅 Weekend Meals Transactions (Sales Dept):")
print(weekend_meals[['date', 'employee', 'vendor', 'amount']])
print("\n" + "="*50 + "\n")

# -----------------------------------------------------
# 5️⃣ Missing Spend Categories Check
# -----------------------------------------------------
missing_categories = ['Software', 'Training']
for cat in missing_categories:
    count = con.execute(f"""
        SELECT COUNT(*) FROM sales_data
        WHERE department = 'Sales' AND category = '{cat}'
    """).fetchone()[0]
    
    if count == 0:
        print(f"❌ No {cat} spend found for Sales")
    else:
        print(f"✅ Found {count} {cat} transaction(s) for Sales")
