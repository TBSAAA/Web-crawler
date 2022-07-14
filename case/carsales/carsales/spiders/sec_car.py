import scrapy


class SecCarSpider(scrapy.Spider):
    name = 'sec_car'
    allowed_domains = ['carsales.com.au']
    start_urls = ['http://carsales.com.au/']

    def parse(self, response):
        pass
