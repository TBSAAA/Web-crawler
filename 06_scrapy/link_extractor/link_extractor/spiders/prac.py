import scrapy
from scrapy.linkextractors import LinkExtractor


class PracSpider(scrapy.Spider):
    name = 'prac'
    allowed_domains = ['che168.com']
    start_urls = ['https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp1exx0/']

    def parse(self, response, **kwargs):
        lk1 = LinkExtractor(restrict_xpaths="//ul[@class='viewlist_ul']/li/a",
                            deny_domains=("topicm.che168.com",))  # 提取详情页的url地址
        links = lk1.extract_links(response)
        for link in links:
            url = link.url
            text = link.text
            # print(url)

        lk2 = LinkExtractor(allow=r"beijing/a0_0msdgscncgpi1ltocsp\d+exx0")
        links = lk2.extract_links(response)
        for link in links:
            print(link.url)
