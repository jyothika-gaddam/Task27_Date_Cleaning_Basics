"""
Task 27: Date Cleaning Basics
Standardizes mixed date formats in a retail sales dataset.
Run from the project root: python scripts/clean_dates.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "retail_sales_raw.csv"
CLEAN_OUTPUT = ROOT / "data" / "retail_sales_cleaned.csv"
ISSUE_OUTPUT = ROOT / "reports" / "date_issue_log.csv"

df = pd.read_csv(INPUT, dtype={"Order_Date_Raw": "string"})
raw = df["Order_Date_Raw"].fillna("").str.strip()

# Parse each value explicitly with pandas' mixed-format support where available.
# dayfirst=False is deliberate because the dataset contains US-style dates such as 01/04/2026.
try:
    parsed = pd.to_datetime(raw.replace("", pd.NA), format="mixed", errors="coerce", dayfirst=False)
except (TypeError, ValueError):  # compatibility with older pandas versions
    parsed = pd.to_datetime(raw.replace("", pd.NA), errors="coerce", dayfirst=False)

df["Order_Date"] = parsed.dt.strftime("%Y-%m-%d")
df["Date_Status"] = "Valid"
df.loc[raw.eq(""), "Date_Status"] = "Missing date"
df.loc[raw.ne("") & parsed.isna(), "Date_Status"] = "Invalid date"

issues = df.loc[df["Date_Status"] != "Valid", ["Order_ID", "Order_Date_Raw", "Date_Status"]].copy()
issues["Issue_Details"] = issues["Date_Status"].map({
    "Missing date": "Date value is blank.",
    "Invalid date": "Could not parse the value as a valid calendar date."
})
issues.to_csv(ISSUE_OUTPUT, index=False)

# Keep the raw date for auditability; the standardized date is ISO YYYY-MM-DD.
df.to_csv(CLEAN_OUTPUT, index=False)

print(f"Rows processed: {len(df)}")
print(f"Valid dates: {(df['Date_Status'] == 'Valid').sum()}")
print(f"Invalid dates: {(df['Date_Status'] == 'Invalid date').sum()}")
print(f"Missing dates: {(df['Date_Status'] == 'Missing date').sum()}")
print(f"Cleaned data saved to: {CLEAN_OUTPUT}")
print(f"Issue log saved to: {ISSUE_OUTPUT}")
