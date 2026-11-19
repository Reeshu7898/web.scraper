
from pathlib import Path

import pandas as pd
from datetime import datetime

base = Path(__file__).resolve().parent
data_path = base / "data" / "books_dataset_clean.csv"
reports_dir = base / "reports"
reports_dir.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv(data_path)

# Start report
report = []

report.append("# EXPLORATORY DATA ANALYSIS REPORT")
report.append("## Books to Scrape Dataset\n")

report.append(f"Report generated: {datetime.now().strftime('%d-%m-%Y %H:%M')}")
report.append("\n---\n")

# 1. Dataset overview
report.append("## 1. DATASET OVERVIEW")
report.append(f"- Total records: {len(df)}")
report.append(f"- Total columns: {len(df.columns)}")
report.append(f"- Columns: {', '.join(df.columns)}")

# 2. Data types
report.append("\n## 2. DATA TYPES")
report.append(df.dtypes.to_string())

# 3. Statistical summary
report.append("\n## 3. STATISTICAL SUMMARY")
report.append(df.describe(include="all").to_string())

# 4. Price analysis
report.append("\n## 4. PRICE ANALYSIS")
report.append(f"- Minimum price: £{df['Price_GBP'].min():.2f}")
report.append(f"- Maximum price: £{df['Price_GBP'].max():.2f}")
report.append(f"- Average price: £{df['Price_GBP'].mean():.2f}")
report.append(f"- Median price: £{df['Price_GBP'].median():.2f}")

# 5. Rating distribution
report.append("\n## 5. RATING DISTRIBUTION")
report.append(df["Rating"].value_counts().sort_index().to_string())

# 6. Data quality
report.append("\n## 6. DATA QUALITY CHECKS")
report.append(f"- Missing values: {df.isnull().sum().sum()}")
report.append(f"- Duplicate records: {df.duplicated().sum()}")
report.append(f"- Invalid ratings: {(~df['Rating'].between(1, 5)).sum()}")

# 7. Outlier analysis
Q1 = df["Price_GBP"].quantile(0.25)
Q3 = df["Price_GBP"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Price_GBP"] < lower) |
    (df["Price_GBP"] > upper)
]

report.append("\n## 7. OUTLIER ANALYSIS")
report.append(f"- Lower IQR limit: £{lower:.2f}")
report.append(f"- Upper IQR limit: £{upper:.2f}")
report.append(f"- Outlier count: {len(outliers)}")

# 8. Availability
report.append("\n## 8. AVAILABILITY ANALYSIS")
report.append(df["Availability"].value_counts().to_string())

# 9. Hypothesis test results
report.append("\n## 9. HYPOTHESIS TESTING")

try:
    with open(reports_dir / "hypothesis_results.txt", "r", encoding="utf-8") as file:
        report.append(file.read())
except FileNotFoundError:
    report.append("Hypothesis results file not found.")

# 10. Conclusion
report.append("\n## 10. FINAL CONCLUSION")
report.append(
    "The dataset contains 20 book records. "
    "The data quality checks identified no missing values, "
    "duplicate records, invalid ratings, or price outliers. "
    "All 20 books are listed as in stock."
)

report.append(
    "\nThe hypothesis test found no statistically significant "
    "evidence of a relationship between book price and rating "
    "in this small synthetic practice dataset."
)

report.append("\n---\n")
report.append("End of EDA Report.")

# Save report
report_path = reports_dir / "EDA_Report.md"
with open(report_path, "w", encoding="utf-8") as file:
    file.write("\n".join(report))

print("EDA REPORT GENERATED SUCCESSFULLY!")
print(f"Report saved as: {report_path}")
