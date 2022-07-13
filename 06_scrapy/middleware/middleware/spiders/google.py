import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com']
    start_urls = ['http://google.com/']

    def parse(self, response, **kwargs):
        print(response.url)
