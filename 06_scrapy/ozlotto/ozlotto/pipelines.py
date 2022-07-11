# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo


# file
class OzlottoPipeline:
    def open_spider(self, spider):
        self.file = open('ozlotto.csv', 'w', encoding='utf-8')
        self.file.write('date,draw_number,main_number,supplementary\n')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(f'{item["date"]},{item["draw_number"]},{item["main_number"]},{item["supplementary"]}\n')
        return item


# mysql
class MySQLPipeline:
    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='jack',
            password='123123',
            database='web_spider',
        )

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cursor = self.connection.cursor()
            draw_number = item['draw_number']
            date = item['date']
            main_number = ",".join(item['main_number'])
            supplementary = ",".join(item['supplementary'])
            sql_insert = f"insert into ozlotto(draw_number, data, main_number, supplementary)" \
                         f" values('{draw_number}', '{date}', '{main_number}', '{supplementary}')"
            self.cursor.execute(sql_insert)
            self.connection.commit()
        except Exception as e:
            print(e)
            if self.cursor:
                self.cursor.close()
            self.connection.rollback()
        return item


# mongodb
class MongoDBPipeline:
    def open_spider(self, spider):
        self.connection = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.connection['crawler_spider']

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.db.ozlotto.insert_one(dict(item))
        return item
