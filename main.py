from CarSpider.CarSpider.spiders.car_spider import startSpider
from sqlite_db import upload_to_sql, upload_to_json
import click


"""
  ________                                  .__   
 /  _____/  ____   ____  _________  __ ____ |  |  
/   \  ___ /  _ \ /  _ \/  ___/\  \/ // __ \|  |  
\    \_\  (  <_> |  <_> )___ \  \   /\  ___/|  |__
 \______  /\____/ \____/____  >  \_/  \___  >____/
        \/                  \/            \/      

"""


@click.group()
def mycommands():
    pass


@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


@click.command()
@click.option('--model', default=None, prompt="Enter car model or write 0", help='Enter the car model or 0 if not applicable')
@click.option('--mileage', default=0, prompt="Enter car mileage in km or write 0", help="Enter the car maximum mileage in km or 0 if not applicable")
@click.option('--price', default=0, prompt="Enter car Price in $ or write 0", help="Enter the car maximum price in $ or 0 if not applicable")
def start_upload(model, mileage, price):
    upload_to_json(price, mileage, model)


@click.command()
def start_scraping():
    startSpider()
    upload_to_sql()


mycommands.add_command(start_upload)
mycommands.add_command(start_scraping)

if __name__ == "__main__":
    click.echo('by goosvel')
    mycommands()
