import redis
import time
import os

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def run_all_collectors():
    collectors = r.keys("collector.*")
    for collector in collectors:
        c = r.hgetall(collector)
        if ("lastrun" not in c):
            c["lastrun"] = 0
    
        now = int(time.time())
        lastrun = int(c["lastrun"])
        interval = int(c["interval"]) 
        script = c["script"]
        params = c["params"]
        if  lastrun + interval < now: 
            print "running ",c["script"]
            os.system("python " + script + " " + params)
            r.hset(collector,"lastrun",now)

while True:
    run_all_collectors()
    time.sleep(10)
