import pymongo

# connection = pymongo.MongoClient("mongodb://localhost")
connection = pymongo.MongoClient(host='localhost', port=27017)

db = connection['crawler_spider']
# insert_one()
# db.test.insert_one({'name': 'test'})
# insert_many()
# db.test.insert_many([{"name": "test", "age": "18"}, {"name": "test2", "age": "19"}])

# search
result = db.test.find({}, {"_id": 0, "age": 1})
for i in result:
    print(i)
