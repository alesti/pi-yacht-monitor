import redis
import time
import os

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.hset("actor.email","script","sendmail.py")
r.hset("actor.email","params","")
r.hset("actor.email","interval",10)
r.hset("actor.email","lastrun",0)
