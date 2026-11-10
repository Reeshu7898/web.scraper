import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")

data = []

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

for book in books:

    title = book.select_one("h3 a")["title"]

    price_text = book.select_one(
        "p.price_color"
    ).text.strip()

    # Remove currency symbol and convert to number
    price = float(
        price_text.replace("£", "").replace("Â", "").strip()
    )

    availability = book.select_one(
        "p.instock.availability"
    ).text.strip()

    rating_class = book.select_one(
        "p.star-rating"
    )["class"]

    rating_word = rating_class[1]

    rating = rating_map[rating_word]

    data.append({
        "Title": title,
        "Price_GBP": price,
        "Rating": rating,
        "Availability": availability
    })

df = pd.DataFrame(data)

df.to_csv(
    "books_dataset_clean.csv",
    index=False,
    encoding="utf-8-sig"
)

print("===================================")
print("WEB SCRAPING COMPLETED")
print("===================================")
print("Total books:", len(df))
print("Dataset saved as: books_dataset_clean.xlsx")
print()
print(df.head())
print()
print("Average price: £", round(df["Price_GBP"].mean(), 2))
print("Average rating:", round(df["Rating"].mean(), 2))