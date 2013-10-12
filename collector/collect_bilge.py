import storagehandler
import sys
import random

if len(sys.argv) != 2:
    print "Usage: collect_bilge.py <sensorname>"
    sys.exit(1)

sensorname = sys.argv[1]


random.seed()

r = random.randint(0,10)

bilge = "dry"

if (r == 1):
    bilge = "full of water"

storagehandler.save("boat." + sensorname,bilge)

