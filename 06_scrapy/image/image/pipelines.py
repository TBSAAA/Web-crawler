# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import scrapy
from scrapy.pipelines.images import ImagesPipeline
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# option 1:
class ImagePipeline:
    def process_item(self, item, spider):
        # resp = requests.get(img_src)
        # resp.content
        # with open(item['img_src'], 'wb') as f:
        #     f.write(resp.content)
        return item


# option 2:
class ImagePipeline_2(ImagesPipeline):
    def get_media_requests(self, item, info):
        url = item['img_src']
        yield scrapy.Request(url)

    def file_path(self, request, response=None, info=None, *, item=None):
        file_path = "main_page/%s" % (item['img_src'].split('/')[-1])
        return file_path

    def item_completed(self, results, item, info):
        print(results)
        return item
