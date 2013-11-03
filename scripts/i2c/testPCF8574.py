#/usr/bin/python

import smbus
import time


# i2c address of PCF8574
PCF8574=0x25

# open the bus (0 -- original Pi, 1 -- Rev 2 Pi)
b=smbus.SMBus(1)

# make certain the pins are set high so they can be used as inputs
b.write_byte(PCF8574, 0x02)

pins = b.read_byte(PCF8574)

if (pins & 0x01) == 0:
    print "Pin 1 ON"
else:
        print "Pin 1 OFF"
if (pins & 0x02) == 0:
    print "Pin 2 ON"
else:
        print "Pin 2 OFF"
if (pins & 0x04) == 0:
    print "Pin 3 ON"
else:
        print "Pin 3 OFF"
if (pins & 0x08) == 0:
    print "Pin 4 ON"
else:
        print "Pin 4 OFF"
if (pins & 0x10) == 0:
    print "Pin 5 ON"
else:
        print "Pin 5 OFF"
if (pins & 0x20) == 0:
    print "Pin 6 ON"
else:
    print "Pin 6 OFF"
if (pins & 0x40) == 0:
    print "Pin 7 ON"
else:
        print "Pin 7 OFF"
if (pins & 0x80) == 0:
    print "Pin 9 ON"
else:
        print "Pin 9 OFF"
