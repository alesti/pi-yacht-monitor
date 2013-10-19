import redis
import time
import os

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def run_all_actors():
    actors = r.keys("actor.*")
    for actor in actors:
        a = r.hgetall(actor)
        if ("lastrun" not in a):
            a["lastrun"] = 0
    
        now = int(time.time())
        lastrun = int(a["lastrun"])
        interval = int(a["interval"]) 
        script = a["script"]
        params = a["params"]
        if  lastrun + interval < now: 
            os.system("python " + script + " " + params)
            r.hset(actor,"lastrun",now)

while True:
    run_all_actors()
    r.hset("system.actor","lastrunn",int(time.time()))
    time.sleep(10)
    
