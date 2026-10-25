import csv
import os
import random
from datetime import date, timedelta

random.seed(42)

NUM_ORDERS = 2000

# name, category, franchise, unit_price, unit_cost, weight
products = [
    ("Luffy Figure 18cm", "Figures", "One Piece", 45, 24, 10),
    ("Goku Figure 20cm", "Figures", "Dragon Ball", 52, 27, 9),
    ("Tanjiro Figure 17cm", "Figures", "Demon Slayer", 48, 25, 8),
    ("Gojo Figure 22cm", "Figures", "Jujutsu Kaisen", 55, 29, 9),
    ("Akatsuki T-Shirt", "Apparel", "Naruto", 25, 10, 12),
    ("Straw Hat Hoodie", "Apparel", "One Piece", 49, 22, 7),
    ("Demon Slayer Haori Jacket", "Apparel", "Demon Slayer", 59, 28, 5),
    ("Survey Corps Hoodie", "Apparel", "Attack on Titan", 54, 25, 6),
    ("One Piece Vol. 1", "Manga", "One Piece", 8, 5, 14),
    ("Jujutsu Kaisen Vol. 1", "Manga", "Jujutsu Kaisen", 8, 5, 10),
    ("My Hero Academia Vol. 1", "Manga", "My Hero Academia", 8, 5, 8),
    ("Naruto Box Set 1", "Manga", "Naruto", 69, 45, 4),
    ("Attack on Titan Poster A3", "Posters", "Attack on Titan", 12, 4, 9),
    ("Dragon Ball Poster A3", "Posters", "Dragon Ball", 12, 4, 8),
    ("Demon Slayer Poster A3", "Posters", "Demon Slayer", 12, 4, 8),
    ("Studio Ghibli Poster A3", "Posters", "Studio Ghibli", 14, 5, 7),
    ("Naruto Headband", "Accessories", "Naruto", 15, 6, 11),
    ("Totoro Keychain", "Accessories", "Studio Ghibli", 9, 3, 10),
    ("Dragon Ball Wallet", "Accessories", "Dragon Ball", 22, 10, 6),
    ("My Hero Academia Mug", "Accessories", "My Hero Academia", 14, 6, 7),
    ("Totoro Plush 30cm", "Plushies", "Studio Ghibli", 32, 15, 9),
    ("Chopper Plush 25cm", "Plushies", "One Piece", 28, 13, 6),
    ("Nezuko Plush 25cm", "Plushies", "Demon Slayer", 29, 13, 6),
    ("All Might Plush 25cm", "Plushies", "My Hero Academia", 30, 14, 4),
]

countries = ["Italy", "Germany", "France", "Spain", "Netherlands", "Belgium", "Poland", "Austria"]
country_weights = [20, 22, 18, 12, 8, 6, 8, 6]

month_weights = [8, 7, 8, 8, 8, 8, 9, 7, 8, 9, 14, 16]

days = [date(2025, 1, 1) + timedelta(days=i) for i in range(365)]
day_weights = [month_weights[d.month - 1] for d in days]

order_dates = sorted(random.choices(days, weights=day_weights, k=NUM_ORDERS))
product_weights = [p[5] for p in products]

rows = []
total_revenue = 0
total_profit = 0

for i, order_date in enumerate(order_dates, start=1):
    product = random.choices(products, weights=product_weights)[0]
    country = random.choices(countries, weights=country_weights)[0]
    quantity = random.choices([1, 2, 3], weights=[70, 22, 8])[0]
    rows.append([
        f"ORD-{i:05d}",
        order_date.isoformat(),
        country,
        product[1],
        product[2],
        product[0],
        quantity,
        product[3],
        product[4],
    ])
    total_revenue += quantity * product[3]
    total_profit += quantity * (product[3] - product[4])

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "anime_merch_sales.csv")

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "order_id", "order_date", "customer_country", "category", "franchise",
        "product_name", "quantity", "unit_price", "unit_cost",
    ])
    writer.writerows(rows)

print("Righe:", len(rows))
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Profit Margin:", round(total_profit / total_revenue * 100, 2), "%")
print("Average Order Value:", round(total_revenue / len(rows), 2))
