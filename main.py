from car_spider import startSpider
from sqlite_db import upload_to_sql, upload_to_json
import click

global model, mileage, price

@click.group()
def mycommands():
    pass

@click.command()
@click.option("--model", prompt="Enter car model", help="Enter car model")
@click.option("--mileage", prompt="Enter car mileage in km", help="Enter car mileage")
@click.option("--price", prompt="Enter car Price in $", help="Enter car price")
def start_upload(model, mileage, price):
    upload_to_json(price, mileage, model)

@click.command()
def start_spider():
    startSpider()
    upload_to_sql()


mycommands.add_command(start_upload)
mycommands.add_command(start_spider)

if __name__ == "__main__":
    mycommands()