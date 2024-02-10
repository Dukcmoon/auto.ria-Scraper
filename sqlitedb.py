import json
import sqlite3
import os
def writedb():
    try:
        os.remove("file/Cars.sqlite")
    except:
        pass


    conn = sqlite3.connect('file/Cars.sqlite')
    cursor = conn.cursor()

    with open('file/Cars.json', 'r') as file:
        data = json.load(file)

    cursor.execute('''CREATE TABLE cars (
                    title TEXT,
                    url TEXT,
                    price INTEGER,
                    mileage INTEGER
                    )''')

    for item in data:
        cursor.execute(f"INSERT INTO cars (title, url, price, mileage) VALUES (?, ?, ?, ?)",
                       (item['Title'], item['URL'], item['Price'], item['Mileage']))
        conn.commit()
    conn.close()

def carimport(Price_filter: None, Mileage_filter: None, Title_filter: None):
    conn = sqlite3.connect('file/Cars.sqlite')
    cursors = conn.cursor()

    cursors.execute("SELECT * FROM cars")
    result = cursors.fetchall()

    json_data = []

    for row in result:
        if Title_filter in row[0]:
            print(row[0])
        else:
            break
        if row[2] <= int(Price_filter):
            print(row[2])
        else:
            break
        if row[3] <= int(Mileage_filter):
            print(row[3])
        else:
            break

        json_data.append({
            'Title': row[0],
            'URL': row[1],
            'Price': row[2],
            'Mileage': row[3]
        })

    with open('file/data.json', 'w') as f:
        json.dump(json_data, f)

    conn.close()