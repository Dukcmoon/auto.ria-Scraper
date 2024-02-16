from CarSpider.CarSpider.spiders.car_spider import startSpider  # spider
from sqlite_db import upload_to_json  # filter
import click


"""
  ________                                  .__   
 /  _____/  ____   ____  _________  __ ____ |  |  
/   \  ___ /  _ \ /  _ \/  ___/\  \/ // __ \|  |  
\    \_\  (  <_> |  <_> )___ \  \   /\  ___/|  |__
 \______  /\____/ \____/____  >  \_/  \___  >____/
        \/                  \/            \/      

"""


@click.group()  # create group
def mycommands():
    pass


@click.command()  # create command filter
@click.option('--model', default=None, prompt="Enter car model or write 0", help='Enter the car model or 0 if not applicable')
@click.option('--mileage', default=0, prompt="Enter car mileage in km or write 0", help="Enter the car maximum mileage in km or 0 if not applicable")
@click.option('--price', default=0, prompt="Enter car Price in $ or write 0", help="Enter the car maximum price in $ or 0 if not applicable")
def start_upload(model, mileage, price):
    upload_to_json(price, mileage, model)


@click.command()  # create command spider
def start_scraping():
    startSpider()


mycommands.add_command(start_upload)  # add command in group
mycommands.add_command(start_scraping)

if __name__ == "__main__":  # entry points
    click.echo('by goosvel')  # my nickname :D
    mycommands()  # start check commands
