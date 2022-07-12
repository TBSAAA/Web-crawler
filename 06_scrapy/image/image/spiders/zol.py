import scrapy
from urllib.parse import urljoin


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/dongman/']

    def parse(self, response, **kwargs):
        a_list = response.xpath("//*[@class='pic-list2  clearfix']/li/a")
        for a in a_list:
            href = a.xpath("./@href").extract_first()
            if href.endswith(".exe"):
                continue
            # href = urljoin(response.url, href)
            href = response.urljoin(href)

            yield scrapy.Request(url=href, method="get", callback=self.parse_detail)

    def parse_detail(self, response, **kwargs):
        img_src = response.xpath("//*[@id='bigImg']/@src").extract_first()
        yield {"img_src": img_src}
