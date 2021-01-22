from redis import Redis

redis_connection = Redis(decode_responses=True)

key ="some-key"
value =100

redis_connection.set(key, value)
print(redis_connection.get(key))

print(redis_connection.incr(key,10))

print(redis_connection.decr(key,20))