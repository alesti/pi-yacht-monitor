import redis
import time
import os

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.hset("config.i2c.analog-in","active",1)
r.hset("config.i2c.analog-in","type","horter-analog-in")
r.hset("config.i2c.analog-in","bus",1)
r.hset("config.i2c.analog-in","address","0x48")
r.hset("config.i2c.analog-in","in0-active",1)
r.hset("config.i2c.analog-in","in0-name","Batterie 1")
r.hset("config.i2c.analog-in","in0-factor",0.04)
r.hset("config.i2c.analog-in","in1-active",1)
r.hset("config.i2c.analog-in","in1-name","Batterie 2")
r.hset("config.i2c.analog-in","in1-factor",0.04)
r.hset("config.i2c.analog-in","in2-active",1)
r.hset("config.i2c.analog-in","in2-name","Batterie 3")
r.hset("config.i2c.analog-in","in2-factor",0.04)
r.hset("config.i2c.analog-in","in3-active",1)
r.hset("config.i2c.analog-in","in3-name","Batterie 4")
r.hset("config.i2c.analog-in","in3-factor",0.04)

r.hset("config.i2c.temp-motor","active",0)
r.hset("config.i2c.temp-motor","type","horter-temp")
r.hset("config.i2c.temp-motor","bus",1)
r.hset("config.i2c.temp-motor","address","0x30")
r.hset("config.i2c.temp-motor","register","0x00")
r.hset("config.i2c.temp-motor","name","Temp-Motor")







