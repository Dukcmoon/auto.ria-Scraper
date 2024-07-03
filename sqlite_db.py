import sqlite3
import json

def upload_to_json(price_filter, mileage_filter, title_filter):
    # Подключение к базе данных
    conn = sqlite3.connect('file/cars.sqlite')
    cur = conn.cursor()

    # Исправление: Добавление запроса для получения данных из таблицы
    cur.execute("SELECT title, url, price, mileage FROM cars")
    rows = cur.fetchall()

    json_data = []

    for row in rows:
        # Фильтрация по заголовку
        if title_filter:
            title_filter_list = list(title_filter.lower())
            if not all(letter in row[0].lower() for letter in title_filter_list):
                continue

        # Фильтрация по цене
        if price_filter:
            if row[2] > int(price_filter):
                continue

        # Фильтрация по пробегу
        if mileage_filter:
            if row[3] > int(mileage_filter):
                continue

        # Добавление данных в json
        json_data.append({
            'Title': row[0],
            'URL': row[1],
            'Price': row[2],
            'Mileage': row[3]
        })

    # Сохранение json в файл
    with open('file/upload.json', 'w') as f:
        json.dump(json_data, f, indent=4)

    # Закрытие подключения к базе данных
    conn.close()
