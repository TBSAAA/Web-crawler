import scrapy


class Game4399Spider(scrapy.Spider):
    name = 'game4399'
    allowed_domains = ['4399.com']
    start_urls = ['https://www.4399.com/flash/gamehw.htm']

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@class="tm_list"]/li')
        for li in li_list:
            game_name = li.xpath('./a//text()').extract_first()
            game_type = li.xpath('./em/a/text()').extract_first()
            game_publish_time = li.xpath('./em/text()').extract_first()
            yield {"game_name": game_name, "game_type": game_type, "game_publish_time": game_publish_time}
