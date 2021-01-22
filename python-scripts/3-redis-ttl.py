from redis import Redis
from time import sleep
from datetime import datetime

redis_connection = Redis(decode_responses=True)

redis_connection.setex("key",9,"Czas")

print(datetime.now().time(), redis_connection.get("key"))
sleep(5)

print(datetime.now().time(), redis_connection.get("key"))
sleep(5)

print(datetime.now().time(), redis_connection.get("key"))


redis_connection.set("key","Czas")
redis_connection.expire("key",9)

print(datetime.now().time(), redis_connection.get("key"))
sleep(5)

print(datetime.now().time(), redis_connection.get("key"))
sleep(5)

print(datetime.now().time(), redis_connection.get("key"))