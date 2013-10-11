import redis

def save(key,value):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set(key,value)
