import pymysql
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='jack',
    password='123123',
    database='web_spider',
)

cur = connection.cursor(DictCursor)
# search data
sql_search = "select * from students;"
cur.execute(sql_search)

# result_all = cur.fetchall()
# print("all",result_all)
result_one = cur.fetchone()
print(result_one)

cur.close()  # disconnect cursor
connection.close()  # disconnect