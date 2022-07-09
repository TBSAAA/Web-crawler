import pymysql

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='jack',
    password='123123',
    database='web_spider',
)

cur = connection.cursor()
# create table
# sql_create = "CREATE TABLE students (id INT(10) AUTO_INCREMENT PRIMARY KEY," \
#       " name VARCHAR(255) not null , age int(3) not null, " \
#       "gender varchar(20), address varchar(255));"

# cur.execute(sql_create)
# print("Created successfully!")

# insert data
sql_insert = "insert into students(name, age, gender, address) values('susu', '28', 'female', 'Sydney');"
result = cur.execute(sql_insert)


connection.commit()
cur.close()  # disconnect cursor
connection.close()  # disconnect

# try:
#     connection.commit()
# except:
#     connection.rollback()