import redis
import time
import os

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

os.system("python collect_bilge.py bilge")
os.system("python collect_temp.py temp")
os.system("python collect_time.py time")
os.system("python collect_voltage.py voltage")

r.hset("config.i2c.analogin","active",1)
r.hset("config.i2c.analogin","type","horter-analog-in")
r.hset("config.i2c.analogin","address","0x48"
r.hset("config.i2c.analogin","bus",1)
r.hset("config.i2c.analogin","in1-active",1)
r.hset("config.i2c.analogin","in2-active",1)
r.hset("config.i2c.analogin","in0-active",1)
r.hset("config.i2c.analogin","in3-active",1)
r.hset("config.i2c.analogin","in0-name","Batterie 1")
r.hset("config.i2c.analogin","in1-name","Batterie 2")
r.hset("config.i2c.analogin","in2-name","Batterie 3")
r.hset("config.i2c.analogin","in3-name","Batterie 4")
r.hset("config.i2c.analogin","in0-factor",0.4)
r.hset("config.i2c.analogin","in1-factor",0.4)
r.hset("config.i2c.analogin","in2-factor",0.4)
r.hset("config.i2c.analogin","in3-factor",0.4)

r.hset("config.i2c.temp-motor","active",1)
r.hset("config.i2c.temp-motor","type","horter-temp")
r.hset("config.i2c.temp-motor","bus",1)
r.hset("config.i2c.temp-motor","address","0x30")
r.hset("config.i2c.temp-motor","name","Temp-Motor")
