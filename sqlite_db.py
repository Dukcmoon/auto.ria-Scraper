import json
import sqlite3
import os

def upload_to_json(price_filter, mileage_filter, title_filter):
    conn = sqlite3.connect('file/Cars.sqlite')
    cursors = conn.cursor()

    cursors.execute("SELECT * FROM cars")
    result = cursors.fetchall()

    json_data = []

    for row in result:

        if title_filter != 0:
            title_filter_list = []
            for letter in title_filter.lower():
                title_filter_list.append(letter)

            if all(elem in row[0].lower() for elem in title_filter_list):
                print(row[0])
            else:
                continue

        if price_filter != 0:
            if row[2] <= int(price_filter):
                print(row[2])
            else:
                continue

        if mileage_filter != 0:
            if row[3] <= int(mileage_filter):
                print(row[3])
            else:
                continue

        json_data.append({
            'Title': row[0],
            'URL': row[1],
            'Price': row[2],
            'Mileage': row[3]
        })

    with open('file/upload.json', 'w') as f:
        json.dump(json_data, f)
    conn.close()
