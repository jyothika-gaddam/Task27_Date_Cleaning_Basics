# Task 27: Date Cleaning Basics

## Objective
Standardize inconsistent date formats in a retail sales dataset and identify missing or invalid dates.

## Tools
- Python
- Pandas
- CSV files (can also be opened in Excel or Google Sheets)

## Project structure
```text
Task27_Date_Cleaning_Basics/
├── data/
│   ├── retail_sales_raw.csv
│   └── retail_sales_cleaned.csv
├── reports/
│   └── date_issue_log.csv
├── scripts/
│   └── clean_dates.py
├── requirements.txt
└── README.md
```

## What was done
1. Created a retail sales dataset containing multiple date formats.
2. Parsed date values explicitly with Pandas.
3. Standardized valid dates to `YYYY-MM-DD`.
4. Flagged missing and invalid dates rather than silently guessing or deleting them.
5. Created an issue log for review and kept the original date column for traceability.

## How to run
Install Python, then open a terminal in this project folder and run:

```bash
python -m pip install -r requirements.txt
python scripts/clean_dates.py
```

The script creates/refreshes `data/retail_sales_cleaned.csv` and `reports/date_issue_log.csv`.

## Important note about ambiguous dates
Dates such as `01/04/2026` can mean January 4 or April 1 depending on regional conventions. This project assumes month-first for slash-separated dates. In a real business dataset, confirm the source's date convention before cleaning.

## Deliverables
- **Clean date column:** `data/retail_sales_cleaned.csv` contains standardized `Order_Date` values.
- **Issue log:** `reports/date_issue_log.csv` lists missing/invalid values for review.

## Interview question: Why are dates often problematic?
Dates may arrive in different formats, use different regional conventions, contain impossible calendar values, or be missing entirely. Standardizing dates improves sorting, filtering, time-based grouping, and analysis accuracy.
