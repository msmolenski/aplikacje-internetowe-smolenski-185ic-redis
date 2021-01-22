from redis import Redis

redis_connection = Redis(decode_responses=True)


key ="17885"
value ="Michal"

redis_connection.set(key, value)
print(redis_connection.get(key))

redis_connection.append(key," to najlepszy student")
print(redis_connection.get(key))

redis_connection.delete(key)
print(redis_connection.get(key))
