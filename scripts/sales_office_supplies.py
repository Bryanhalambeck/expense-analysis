# ============================================================
# 📊 sales_office_supplies.py
# ------------------------------------------------------------
"""
This script dives into Office Supplies spending within the Sales department
of a small company. It helps flag potential issues like outlier employees,
overused vendors, outlier transactions, or unusual timing.

📘 How it works:
- We zoom in on all Office Supplies expenses tied to the Sales team.
- We highlight outliers in employee and vendor spend using z-scores.
- We break down monthly trends and spot transactions on weekends/holidays.
- We visualize spending splits with bar charts, pie charts, and strip plots.

The goal is to surface potential overspending or fairness issues —
and give a clear, visual window into how this category is being used.
"""

# ---------------------------
# 1️⃣ Imports
# ---------------------------
import pandas as pd
import duckdb
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# ---------------------------
# 2️⃣ Load and Prepare Data
# ---------------------------
df = pd.read_csv('data/SmallCompany.csv')
df['date'] = pd.to_datetime(df['date'], format="%m/%d/%y", errors='coerce')
df['day_of_week'] = df['date'].dt.dayofweek
df['day_type'] = df['day_of_week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
df['month'] = df['date'].dt.to_period('M').astype(str)

us_holidays = pd.to_datetime([
    "2024-07-04", "2024-09-02", "2024-11-28", "2024-12-25",
    "2025-01-01", "2025-01-20", "2025-02-17", "2025-05-26", "2025-07-04"
])
df['is_holiday'] = df['date'].isin(us_holidays)

# ---------------------------
# 3️⃣ Subset: Sales – Office Supplies
# ---------------------------
con = duckdb.connect()
con.register("sales_data", df)

sales_os = con.execute("""
    SELECT * FROM sales_data
    WHERE department = 'Sales' AND category = 'Office Supplies'
""").df()

# ---------------------------
# 4️⃣ Employee Spend Analysis
# ---------------------------
emp_total = sales_os.groupby('employee')['amount'].sum()
emp_z = zscore(emp_total)
emp_outliers = emp_total[abs(emp_z) > 1.0]

print("👤 Employee Spend:")
print(emp_total.sort_values(ascending=False))
if not emp_outliers.empty:
    print("\n🚩 Employee Outliers (z > 1.0):")
    for name, amt in emp_outliers.items():
        print(f"{name}: ${amt:.2f}")
print("\n" + "="*50 + "\n")

# ---------------------------
# 5️⃣ Vendor Spend Analysis
# ---------------------------
vendor_total = sales_os.groupby('vendor')['amount'].sum()
vendor_z = zscore(vendor_total)
vendor_outliers = vendor_total[abs(vendor_z) > 1.5]

print("🏪 Vendor Spend:")
print(vendor_total.sort_values(ascending=False))
if not vendor_outliers.empty:
    print("\n🚩 Vendor Outliers (z > 1.5):")
    for name, amt in vendor_outliers.items():
        print(f"{name}: ${amt:.2f}")
print("\n" + "="*50 + "\n")

# ---------------------------
# 6️⃣ Monthly Spend Trend
# ---------------------------
monthly_trend = sales_os.groupby('month')['amount'].sum()
print("📅 Monthly Spend:")
print(monthly_trend.reset_index(name='Monthly Spend ($)'))

monthly_trend.plot(kind='line', marker='o', figsize=(10, 4))
plt.title('Sales – Office Supplies Monthly Spend')
plt.ylabel('Amount ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

# ---------------------------
# 7️⃣ Transaction-Level Outliers
# ---------------------------
sales_os['z_score'] = zscore(sales_os['amount'])
txn_outliers = sales_os[sales_os['z_score'].abs() > 1.5]

print("🚨 Transaction-Level Outliers (z > 1.5):")
print(txn_outliers[['date', 'employee', 'vendor', 'amount', 'z_score']])
print("\n" + "="*50 + "\n")

# ---------------------------
# 8️⃣ Weekend / Holiday Checks
# ---------------------------
weekend_txns = sales_os[sales_os['day_type'] == 'Weekend']
holiday_txns = sales_os[sales_os['is_holiday']]

if not weekend_txns.empty:
    print("🗓️ Weekend Transactions:")
    print(weekend_txns[['date', 'employee', 'vendor', 'amount']].sort_values('date'))
else:
    print("✅ No weekend transactions.")

if not holiday_txns.empty:
    print("\n🎉 Holiday Transactions:")
    print(holiday_txns[['date', 'employee', 'vendor', 'amount']].sort_values('date'))
else:
    print("✅ No holiday transactions.")
print("\n" + "="*50 + "\n")

# ---------------------------
# 9️⃣ Bar Chart: % Spend by Employee
# ---------------------------
emp_summary = sales_os.groupby('employee')['amount'].sum().reset_index()
emp_summary['percent_of_total'] = emp_summary['amount'] / emp_summary['amount'].sum() * 100
emp_summary['z_score'] = zscore(emp_summary['percent_of_total'])
emp_summary = emp_summary.sort_values('percent_of_total', ascending=False)

plt.figure(figsize=(10, 6))
bars = plt.bar(emp_summary['employee'], emp_summary['percent_of_total'], color='skyblue')

for bar, z in zip(bars, emp_summary['z_score']):
    if abs(z) > 1.0:  # Use z > 1.0 for flagging
        bar.set_color('orange')

plt.axhline(100 / emp_summary.shape[0], color='red', linestyle='--', label='Expected Share')
plt.title('Sales – Office Supplies Spend by Employee')
plt.ylabel('Percent of Total Spend')
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ---------------------------
# 🔟 Pie Chart: Vendor Breakdown
# ---------------------------
vendor_data = sales_os.groupby('vendor')['amount'].sum().reset_index()

plt.figure(figsize=(6, 6))
plt.pie(vendor_data['amount'], labels=vendor_data['vendor'],
        autopct='%1.1f%%', startangle=140,
        colors=sns.color_palette("pastel"))

plt.title('Sales – Office Supplies Vendor Breakdown')
plt.tight_layout()
plt.show()

# ---------------------------
# 1️⃣1️⃣ Transaction Strip Plot (Z-Scores)
# ---------------------------
tx_data = sales_os[['employee', 'amount']].copy()
mean_amt = tx_data['amount'].mean()
std_amt = tx_data['amount'].std()
tx_data['highlight'] = tx_data['employee'].apply(lambda x: 'David Kim' if x == 'David Kim' else 'Other')

plt.figure(figsize=(12, 6))
sns.stripplot(data=tx_data, x='employee', y='amount',
              hue='highlight', palette={'David Kim': 'red', 'Other': 'gray'},
              size=12, jitter=False, alpha=0.8, zorder=3)

for i in range(3):
    y_val = mean_amt + i * std_amt
    plt.axhline(y_val, color='blue', linestyle='--', linewidth=1.2)
    label = f"{'Mean (0 SD)' if i == 0 else f'+{i} SD'}"
    plt.text(len(tx_data['employee'].unique()), y_val + 5, label,
             color='blue', fontsize=10, va='bottom')

plt.title("Sales – Office Supplies Transaction Z-Score Outlier")
plt.ylabel("Transaction Amount ($)")
plt.xlabel("Employee")
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.legend(title='Legend', loc='upper left')
plt.tight_layout()
plt.show()
