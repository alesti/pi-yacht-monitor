import storagehandler
import sys
import random

if len(sys.argv) != 2:
    print "Usage: collect_temp.py <sensorname>"
    sys.exit(1)

sensorname = sys.argv[1]


random.seed()

temperature = random.randint(0,280)/10.

storagehandler.save("boat." + sensorname,temperature)

