import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set("boat.voltage",12.5)
r.set("boat.temperature",14.5)
r.set("boat.bilge","dry")
