import os

from CarSpider.runner import start_spider
from upload_filtered_cars_to_json import upload_to_json
import click


settings_file_path = 'CarSpider.CarSpider.settings'
os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)


@click.group()  # create group
def mycommands():
    pass


@click.command()  # create command filter
@click.option('--model', default=None, prompt="Enter car model or write 0", help='Enter the car model or 0 if not applicable')
@click.option('--mileage', default=0, prompt="Enter car mileage in km or write 0", help="Enter the car maximum mileage in km or 0 if not applicable")
@click.option('--price', default=0, prompt="Enter car Price in $ or write 0", help="Enter the car maximum price in $ or 0 if not applicable")
def upload(model, mileage, price):
    upload_to_json(price, mileage, model)


@click.command()  # create command spider
def scrapy():
    start_spider()


mycommands.add_command(upload)  # add command in group
mycommands.add_command(scrapy)


if __name__ == "__main__":  # entry points
    click.echo('by goosvel')
    mycommands()  # start check commands
