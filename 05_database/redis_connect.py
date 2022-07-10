import redis
import json

red = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
# red.set('who', 'jack')
# red.save()
# print(red.get('who'))

# red.hset('user', 'name', 'jack')
# red.hset('user', 'age', '18')
# red.save()
# print(red.hmget('user', 'name', 'age'))
# print(red.hgetall('user'))

# red.lpush('kaka', 'jack', 'tom', 'jerry')
# print(red.lrange('kaka', 0, -1))

# red.sadd('student', 'jack', 'tom', 'jerry', 'james')
# print(red.smembers('student'))

# red.zadd('exam', {'jack': 100, 'tom': 90, 'jerry': 80, 'james': 70})
# print(red.zrange('exam', 0, -1, withscores=True))


# lst = ["jack", "tom", "jerry", "james"]
# red.set("list_prac", json.dumps(lst))
# print(red.get("list_prac"))
#
# red.save()
# red.close()