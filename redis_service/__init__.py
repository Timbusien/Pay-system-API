import redis

redis_my_db = redis.from_url('redis://localhost')

redis_my_db.set('name', 'Rustam')
data = redis_my_db.get('name')
print(data)
