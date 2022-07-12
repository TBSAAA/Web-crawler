import scrapy
from pagination.items import PaginationItem


class NovelPaginationSpider(scrapy.Spider):
    name = 'novel_pagination'
    allowed_domains = ['17k.com']
    start_urls = ['https://www.17k.com/all/book/2_0_0_0_0_0_0_0_1.html']

    def parse(self, response, **kwargs):
        trs = response.xpath("//tbody/tr")
        for tr in trs:
            item = PaginationItem()
            novel_type = tr.xpath(".//*[@class='td2']//text()").extract()
            if not novel_type:
                continue
            novel_name = tr.xpath(".//*[@class='td3']//text()").extract()
            novel_current_word = tr.xpath(".//*[@class='td5']//text()").extract_first()
            novel_author = tr.xpath(".//*[@class='td6']/a/text()").extract_first()

            item['novel_current_word'] = novel_current_word
            item['novel_author'] = novel_author
            item['novel_type'] = novel_type[1]
            item['novel_name'] = novel_name[2]
            yield item

        hrefs = response.xpath("//div[@class='page']/a/@href").extract()
        for href in hrefs:
            if not href.endswith("html"):
                continue
            href = response.urljoin(href)
            yield scrapy.Request(
                url=href,
                callback=self.parse,
            )
