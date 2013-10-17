import redis
import time

def save(key,value):
    timestamp = int(time.time())
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.hset(key,"value",value)
    r.hset(key,"time",timestamp)

