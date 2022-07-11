import scrapy
from ozlotto.items import OzlottoItem

class GetOzlottoSpider(scrapy.Spider):
    name = 'get_ozlotto'
    allowed_domains = ['ozlotteries.com']
    start_urls = ['https://www.ozlotteries.com/oz-lotto/results/june-2021']

    def parse(self, response, **kwargs):
        divs = response.xpath('//*[@data-id="drawResultStacked_Root"]')
        for div in divs:
            item = OzlottoItem()
            item['date'] = div.xpath('.//h4/text()').extract_first()
            item['draw_number'] = div.xpath('.//h4/span/text()').extract_first().split(' ')[1]
            item['main_number'] = div.xpath('.//*[@class="results-number-set__number--ns1 css-jreslj-Root eik1jin0"]/text()').extract()
            item['supplementary'] = div.xpath('.//*[@class="results-number-set__number--ns2 css-ciftkg-Root eik1jin0"]/text()').extract()
            yield item
