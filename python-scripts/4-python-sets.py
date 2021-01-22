from redis import Redis

redis_connection = Redis(decode_responses=True)

#Posortowane zbiory

redis_connection.zadd("sorted_set_key",{"key1": 4})
redis_connection.zadd("sorted_set_key",{"key2": 3})
redis_connection.zadd("sorted_set_key",{"key3": 2})
redis_connection.zadd("sorted_set_key",{"key4": 1})

print(redis_connection.zrange("sorted_set_key",0, -1))

#Hashe

hash_key ='tertowy_hash'

redis_connection.hset(hash_key,'key','value')