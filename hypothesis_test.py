from pathlib import Path
import pandas as pd
from scipy import stats

# Find the CSV relative to this script, not the terminal folder.
base = Path(__file__).resolve().parent
candidates = [
    base / "books_dataset_clean.csv",
    base / "data" / "books_dataset_clean.csv",
]
csv_path = next((p for p in candidates if p.is_file()), None)

if csv_path is None:
    raise FileNotFoundError(
        "Put books_dataset_clean.csv inside the data folder."
    )

raw = pd.read_csv(csv_path)
columns = ["Price_GBP", "Rating"]
if not set(columns).issubset(raw.columns):
    raise ValueError(f"Expected columns {columns}; found {list(raw.columns)}")

# Keep complete, numeric, finite price-rating pairs.
pairs = raw[columns].apply(pd.to_numeric, errors="coerce")
pairs = pairs.replace([float("inf"), -float("inf")], float("nan"))
pairs = pairs.dropna()

if len(pairs) < 3 or (pairs.nunique() < 2).any():
    raise ValueError("Need at least 3 valid rows and variation in both columns.")

prices = pairs["Price_GBP"].to_numpy()
ratings = pairs["Rating"].to_numpy()


def correlation(shuffled_prices):
    # Use only the coefficient, not spearmanr's approximate p-value.
    return stats.spearmanr(shuffled_prices, ratings).statistic


print("Calculating the permutation test...")
result = stats.permutation_test(
    (prices,),
    correlation,
    permutation_type="pairings",
    vectorized=False,
    n_resamples=9999,
    alternative="two-sided",
    rng=42,
)

report = (
    "PRICE-RATING HYPOTHESIS TEST\n"
    f"Books used: {len(pairs)}\n"
    f"Rows excluded: {len(raw) - len(pairs)}\n"
    f"Spearman rho: {result.statistic:.3f}\n"
    f"Two-sided permutation p-value: {result.pvalue:.4f}\n"
    "Scope: synthetic practice data, not real book-market evidence.\n"
)
print(report)

reports_dir = base / "reports"
reports_dir.mkdir(exist_ok=True)
output = reports_dir / "hypothesis_results.txt"
output.write_text(report, encoding="utf-8")
print(f"Report saved to: {output}")