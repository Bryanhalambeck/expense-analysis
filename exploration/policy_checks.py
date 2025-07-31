# =====================================================
# 📊 policy_checks.py
# -----------------------------------------------------

import pandas as pd

# -----------------------------------------------------
# 1️⃣ Load Expense Data
# -----------------------------------------------------
df = pd.read_csv("Untitledspreadsheet72.csv")

# -----------------------------------------------------
# 2️⃣ Meals Policy: Max $55 per meal per employee
# -----------------------------------------------------
df_meals_over = df[
    (df['category'] == 'Meals') &
    (df['amount'] > 55)
]

# -----------------------------------------------------
# 3️⃣ Travel Policy: Max $855 per day per employee
# -----------------------------------------------------
df_travel = df[df['category'] == 'Travel']
daily_travel = df_travel.groupby(['employee', 'date'])['amount'].sum().reset_index()
daily_travel_over = daily_travel[daily_travel['amount'] > 855]

# -----------------------------------------------------
# 4️⃣ Training Policy: Max $1,400 per employee per course
# -----------------------------------------------------
df_training_over = df[
    (df['category'] == 'Training') &
    (df['amount'] > 1400)
]

# -----------------------------------------------------
# 5️⃣ Office Supplies Policy: Any transaction > $650
# -----------------------------------------------------
df_office_supplies_over = df[
    (df['category'] == 'Office Supplies') &
    (df['amount'] > 650)
]

# -----------------------------------------------------
# 6️⃣ Software Policy: New software > $2,000 requires approval
# -----------------------------------------------------
df_software_over = df[
    (df['category'] == 'Software') &
    (df['amount'] > 2000)
]

# -----------------------------------------------------
# 7️⃣ Display Flagged Policy Violations
# -----------------------------------------------------
print("🚩 Meals Policy Violations:\n", df_meals_over)
print("\n🚩 Travel Policy Violations:\n", daily_travel_over)
print("\n🚩 Training Policy Violations:\n", df_training_over)
print("\n🚩 Office Supplies Policy Violations:\n", df_office_supplies_over)
print("\n🚩 Software Policy Violations:\n", df_software_over)

# -----------------------------------------------------
# (Optional) Save to CSV (Uncomment to export)
# -----------------------------------------------------
# df_meals_over.to_csv("outputs/policy_meals_over.csv", index=False)
# daily_travel_over.to_csv("outputs/policy_travel_over.csv", index=False)
# df_training_over.to_csv("outputs/policy_training_over.csv", index=False)
# df_office_supplies_over.to_csv("outputs/policy_office_supplies_over.csv", index=False)
# df_software_over.to_csv("outputs/policy_software_over.csv", index=False)
