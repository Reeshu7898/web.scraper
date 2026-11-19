# Books Web Scraper and Analysis

This project scrapes book listings from [Books to Scrape](https://books.toscrape.com/), then explores the cleaned dataset with data-quality checks, visualizations, and a price-rating hypothesis test.

## Project layout

```text
web.scraper/
├── README.md
├── scraper.py
├── eda.py
├── data_quality.py
├── hypothesis_test.py
├── eda_report.py
├── data/
│   ├── books_dataset.csv
│   └── books_dataset_clean.csv
├── reports/
│   ├── EDA_Report.md
│   └── hypothesis_results.txt
├── visualizations/
│   ├── book_price_distribution.png
│   ├── book_rating_distribution.png
│   ├── book_price_vs_rating.png
│   ├── price_distribution.png
│   ├── rating_distribution.png
│   └── price_vs_rating.png
└── requirements.txt
```

The unprefixed chart files are older exports retained from the existing project; `eda.py` generates the `book_*.png` charts.

## Setup and run

From the project directory:

```bash
python -m pip install -r requirements.txt
python scraper.py
python data_quality.py
python eda.py
python hypothesis_test.py
python eda_report.py
```

The scraper writes the refreshed cleaned dataset to `data/books_dataset_clean.csv`. Analysis scripts read from `data/`, charts are saved in `visualizations/`, and generated reports are saved in `reports/`. The scripts resolve these paths relative to their own location, so they can also be launched from another working directory.

`data/books_dataset.csv` is the original source snapshot; the scraper generates the normalized cleaned dataset separately.
