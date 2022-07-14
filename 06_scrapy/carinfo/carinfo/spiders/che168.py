import scrapy


class Che168Spider(scrapy.Spider):
    name = 'che168'
    allowed_domains = ['che168.com']
    start_urls = ['https://www.che168.com/china/a0_0msdgscncgpi1ltocsp1exx0/']

    # map
    car_info = {
        "表显里程": "odometer",
        "上牌时间": "build_date",
        "挡位/排量": "transmission",
        "车辆所在地": "location",
        "查看限迁地": "standard",
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@class="viewlist_ul"]/li')
        for li in li_list:
            href = li.xpath('./a/@href').extract_first()
            href = response.urljoin(href)
            if "topicm" in href:
                continue
            yield scrapy.Request(
                href,
                callback=self.parse_detail
            )
        hrefs = response.xpath('//*[@id="listpagination"]/a/@href').extract()
        for href in hrefs:
            if href.startswith('javascript'):
                continue
            href = response.urljoin(href)
            yield scrapy.Request(
                href,
                callback=self.parse
            )

    def parse_detail(self, response, **kwargs):
        print(response.url)
        title = response.xpath('//*[@class="car-box"]/h3/text()').extract_first()
        li_list = response.xpath('//*[@class="car-box"]/ul/li')
        dic = {
            'odometer': 'unknown',
            'build_date': 'unknown',
            'transmission': 'unknown',
            'engine': 'unknown',
            'location': 'unknown',
            'standard': 'unknown',
        }
        for li in li_list:
            p_name = li.xpath("./p//text()").extract_first()
            p_value = li.xpath("./h4/text()").extract_first()
            p_name = p_name.replace(' ', '').strip()
            p_value = p_value.replace(' ', '').strip()

            data_key = self.car_info.get(p_name)

            if data_key == 'transmission':
                dic['transmission'] = p_value.split('/')[0]
                dic['engine'] = p_value.split('/')[1]
            else:
                dic[data_key] = p_value
        yield dic