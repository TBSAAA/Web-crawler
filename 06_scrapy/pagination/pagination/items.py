# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaginationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    novel_current_word = scrapy.Field()
    novel_author = scrapy.Field()
    novel_name = scrapy.Field()
    novel_type = scrapy.Field()
