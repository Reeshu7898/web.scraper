
from pathlib import Path

import pandas as pd

# Load the cleaned dataset
base = Path(__file__).resolve().parent
df = pd.read_csv(base / "data" / "books_dataset_clean.csv")

# 1. Dataset dimensions
print("\n--- DATASET SHAPE ---")
print(df.shape)

# 2. Column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# 3. First five records
print("\n--- FIRST FIVE RECORDS ---")
print(df.head())

# 4. Dataset information
print("\n--- DATASET INFORMATION ---")
df.info()

# 5. Statistical summary
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe(include="all"))


# 6. Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 7. Check duplicate records
print("\n--- DUPLICATE RECORDS ---")
print(df.duplicated().sum())

# 8. Check dataset data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# 9. Check price range
print("\n--- PRICE ANALYSIS ---")
print("Minimum price:", df["Price_GBP"].min())
print("Maximum price:", df["Price_GBP"].max())
print("Average price:", df["Price_GBP"].mean())

# 10. Check rating distribution
print("\n--- RATING DISTRIBUTION ---")
print(df["Rating"].value_counts().sort_index())


# 8. DATA VISUALIZATION

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
visualizations = base / "visualizations"
visualizations.mkdir(exist_ok=True)

# Graph 1: Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Price_GBP", bins=8, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (GBP)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig(
    visualizations / "book_price_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Graph 2: Rating Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Rating")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig(
    visualizations / "book_rating_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Graph 3: Price vs Rating
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Rating", y="Price_GBP")
plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (GBP)")
plt.tight_layout()
plt.savefig(
    visualizations / "book_price_vs_rating.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

print("\nAll visualizations generated successfully!")


# 9. OUTLIER DETECTION USING IQR

Q1 = df["Price_GBP"].quantile(0.25)
Q3 = df["Price_GBP"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Price_GBP"] < lower_limit) |
    (df["Price_GBP"] > upper_limit)
]

print("\n--- OUTLIER ANALYSIS ---")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nDetected Outliers:")
print(outliers[["Title", "Price_GBP"]])

print("\nTotal Outliers:", len(outliers))
