# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


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
            novel_name = item['novel_name']
            novel_type = item['novel_type']
            novel_author = item['novel_author']
            novel_current_word = item['novel_current_word']
            sql_insert = f"insert into novel(name, type, author, current_word)" \
                         f" values('{novel_name}', '{novel_type}', '{novel_author}', '{novel_current_word}')"
            self.cursor.execute(sql_insert)
            self.connection.commit()
        except Exception as e:
            print(e)
            if self.cursor:
                self.cursor.close()
            self.connection.rollback()
        return item

