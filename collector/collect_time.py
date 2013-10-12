import time
import storagehandler
import sys

if len(sys.argv) != 2:
    print "Usage: collect_time.py <sensorname>"
    sys.exit(1)

sensorname = sys.argv[1]

timestamp = int(time.time())
storagehandler.save("boat." + sensorname,timestamp)

