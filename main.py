from CarSpider import startSpider
from sqlitedb import writedb, carimport
import click

@click.command()
@click.option("--model", prompt="Enter car model", help="Enter car model")
@click.option("--mileage", prompt="Enter car mileage", help="Enter car mileage")
@click.option("--price", prompt="Enter car Price", help="Enter car price")
def setiings(model, mileage, price):
    print(f"""
        car model: {model}
        car mileage: {mileage}
        car Price: {price}
        
    """)
    startSpider()
    writedb()
    carimport(price, mileage, model)



if __name__ == "__main__":
    setiings()



