import redis
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.hset("collector.voltage","script","collect_voltage.py")
r.hset("collector.voltage","params","voltage")
r.hset("collector.voltage","interval",10)
r.hset("collector.voltage","lastrun",0)

r.hset("collector.temp","script","collect_temp.py")
r.hset("collector.temp","params","temp")
r.hset("collector.temp","interval",20)
r.hset("collector.temp","lastrun",0)

r.hset("collector.bilge","script","collect_bilge.py")
r.hset("collector.bilge","params","bilge")
r.hset("collector.bilge","interval",30)
r.hset("collector.bilge","lastrun",0)

r.hset("collector.time","script","collect_time.py")
r.hset("collector.time","params","time")
r.hset("collector.time","interval",40)
r.hset("collector.time","lastrun",0)

