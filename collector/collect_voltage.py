import storagehandler
import sys
import random

if len(sys.argv) != 2:
    print "Usage: collect_voltage.py <sensorname>"
    sys.exit(1)

sensorname = sys.argv[1]


random.seed()

voltage = random.randint(100,140)/10.

storagehandler.save("boat." + sensorname,voltage)

