import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='jack',
    password='123123',
    database='web_spider',
)

cur = connection.cursor()
# search data
sql_search = "select * from students;"
cur.execute(sql_search)

# result_all = cur.fetchall()
# print("all",result_all)
result_one = cur.fetchone()
print("one",result_one)