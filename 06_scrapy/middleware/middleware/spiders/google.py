import scrapy
from middleware.req import SeleniumRequest


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com']
    start_urls = ['https://www.zhipin.com/web/geek/job?query=python&city=100010000']

    def start_requests(self):
        yield SeleniumRequest(url=self.start_urls[0], callback=self.parse, dont_filter=True)
        yield scrapy.Request(url="www.google.com")

    def parse(self, response, **kwargs):
        print(response.text)
