import sqlite3
import json

def upload_to_json(price_filter, mileage_filter, title_filter):
    # Connecting to the database
    conn = sqlite3.connect('cars.sqlite')
    cur = conn.cursor()

    # Fix: Add a query to fetch data from the table
    cur.execute("SELECT title, url, price, mileage FROM cars")
    rows = cur.fetchall()

    json_data = []

    for row in rows:
        # Filtering by title
        if title_filter:
            title_filter_list = list(title_filter.lower())
            if not all(letter in row[0].lower() for letter in title_filter_list):
                continue

        # Filtering by price
        if price_filter:
            if price_filter == 0:
                continue
            elif int(row[2]) > int(price_filter):
                continue

        # Filtering by mileage
        if mileage_filter:
            if mileage_filter == 0:
                continue
            if int(row[3]) > int(mileage_filter):
                continue

        # Adding data to json
        json_data.append({
            'Title': row[0],
            'URL': row[1],
            'Price': row[2],
            'Mileage': row[3]
        })

    # Saving json to a file
    with open('upload.json', 'w') as f:
        json.dump(json_data, f, indent=4)

    # Closing the database connection
    conn.close()
