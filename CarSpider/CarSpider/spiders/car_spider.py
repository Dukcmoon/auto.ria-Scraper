import scrapy


class CarSpiderSpider(scrapy.Spider):
    name = "CarSpider"
    allowed_domains = ['auto.ria.com']
    start_urls = ["https://auto.ria.com/car/used/"]

    def parse(self, response):
        for content in response.css('div.content'):
            yield {
                'URL': content.css('a.address').attrib['href'],
                'Title': content.css('span.blue.bold::text').get(),
                'Price': content.css('span.bold.size22.green::text').get().replace(" ", ""),
                'Mileage': content.css('li.item-char.js-race::text').get().replace(' тыс. км', '')
            }

        next_page = response.css('a.page-link.js-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
