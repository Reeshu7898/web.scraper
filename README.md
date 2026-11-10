# Books to Scrape Web Scraper

A small Python scraper that collects book information from [Books to Scrape](https://books.toscrape.com/), a site intended for scraping practice.

## What it does

- Fetches the catalog page with requests.
- Parses book listings with Beautiful Soup.
- Collects each book's title, price in GBP, star rating, and availability.
- Converts star ratings to numbers and saves the results to a CSV file.
- Prints the number of books and average price and rating.

## Requirements

- Python 3
- requests
- beautifulsoup4
- pandas

## Setup

Install the dependencies:

```bash
python -m pip install requests beautifulsoup4 pandas
```

## Run

From the directory containing scraper.py, run:

```bash
python scraper.py
```

## Output

The script creates books_dataset_clean.csv in the current working directory. The CSV contains these columns:

| Column | Description |
| --- | --- |
| Title | Book title |
| Price_GBP | Price in pounds sterling |
| Rating | Star rating from 1 to 5 |
| Availability | Availability text shown on the page |

The scraper currently processes the books listed on the catalog page; it does not follow pagination.
