import pandas as pd

# Load Excel File

df = pd.read_excel("data/disbursal_Sheet.xlsx")

# Remove Duplicates

df = df.drop_duplicates()

# Convert Date Column

df["Disbursal Date"] = pd.to_datetime(
df["Disbursal Date"],
errors="coerce"
)

# Remove Unnecessary Columns

df = df.drop(
columns=[
"Loan Cancel Closure Date",
"Payment Account Type",
"Payment Account Name",
"Instrument Number",
"Nature Of Loan"
],
errors="ignore"
)
# Unique value
print(df["Category"].unique())

# Fill null value
df.fillna("N/A")

# Save Clean Data

df.to_csv(
"data/cleaned_finance_data.csv",
index=False
)

print("Data Cleaned Successfully")
