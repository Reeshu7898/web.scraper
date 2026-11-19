
from pathlib import Path

import pandas as pd

# Load cleaned dataset
base = Path(__file__).resolve().parent
df = pd.read_csv(base / "data" / "books_dataset_clean.csv")

print("\n===== DATA QUALITY ANALYSIS =====")

# 1. Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 2. Duplicate records
print("\n--- DUPLICATE RECORDS ---")
print("Duplicates:", df.duplicated().sum())

# 3. Invalid ratings
print("\n--- INVALID RATINGS ---")
invalid_ratings = df[
    ~df["Rating"].between(1, 5)
]
print(invalid_ratings)

# 4. Price outliers using IQR
print("\n--- PRICE OUTLIERS ---")

Q1 = df["Price_GBP"].quantile(0.25)
Q3 = df["Price_GBP"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Price_GBP"] < lower_limit) |
    (df["Price_GBP"] > upper_limit)
]

print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Outlier records:")
print(outliers[["Title", "Price_GBP"]])

# 5. Availability check
print("\n--- AVAILABILITY VALUES ---")
print(df["Availability"].value_counts())

print("\n===== ANALYSIS COMPLETED =====")
