# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class CarSpiderPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('file/cars.sqlite')
        self.cur = self.conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        URL TEXT,  
        Title TEXT,  
        Price TEXT, 
        Mileage TEXT)"""
        self.cur.execute(create_table_query)
        self.conn.commit()
        print("Таблица успешно создана")

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO Cars (URL, Title, Price, Mileage) VALUES (?, ?, ?, ?)",
                             (item['URL'], item['Title'], item['Price'], item['Mileage']))
            self.conn.commit()
            print("Данные успешно добавлены")
        except Exception as e:
            print(f"Ошибка при добавлении данных: {e}")
        return item
