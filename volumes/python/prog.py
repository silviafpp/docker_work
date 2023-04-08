import redis

r = redis.Redis(host='redis', port=6379, db=0)
r.set('mykey', 'OLA')
print(r.get('mykey'))