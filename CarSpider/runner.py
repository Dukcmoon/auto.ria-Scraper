from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from CarSpider.CarSpider.spiders.car_spider import CarSpiderSpider


def start_spider():

    try:
        process = CrawlerProcess(settings=get_project_settings())
        process.crawl(CarSpiderSpider)
        process.start()
    except Exception as e:
        print(f"An error occurred: {e}")
