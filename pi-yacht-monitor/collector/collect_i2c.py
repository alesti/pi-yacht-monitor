#!/usr/bin/python
import storagehandler
import sys
import redis
from smbus import SMBus
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)


# reads data from horter-analog-in-card
# converts it with factor to human-readable voltage
# save in redis with name from config
def readPCF8591(config):
    print "Now reading HorterAnalogIn"
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = SMBus(busnumber)
    
    for i in range(0,4):
        port = "in"+str(i) + "-"
        in_active = config[port + "active"]
        if in_active == "1":
            in_factor = float(config[port + "factor"])
            in_name   = config[port + "name"]
            value = int("0x0" + str(i),16)
            bus.write_byte(address,value)
            time.sleep(0.1)
            bus.read_byte(address)
            time.sleep(0.1)
            voltage_raw = bus.read_byte(address)
            voltage = round(voltage_raw * in_factor,2)
            storagehandler.save("boat." + in_name,voltage)


# reads data from horter-temp-sensor
# converts to human-readable temp
# save in redis with name from config
def readLM75(config):
    print "Now reading HorterTemp"
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    name = config["name"]
    bus = SMBus(busnumber)
    raw_temp = bus.read_word(address)
    vorkomme = raw_temp & 0xFF
    nachkomma = raw_temp >> 15
    temp = 0
    if (vorkomma & 0x80) != 0x80:
        temp = vorkomma + nachkomma * 0.5
    else:
        vorkomma = -((~vorkomma & 0xFF) + 1)
        temp = vorkomma + nachkomma * 0.5
    storagehandler.save("boat." + name,temp)

def readPCF8574_IN(config):
    print "Now reading DigitalIn"
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = SMBus(busnumber)
    state = bus.read_byte(address)
    for i in range(0,8):
        port = "in" + str(i) + "-"
        in_active = config[port + "active"]
        if in_active == "1":
            in_name = config[port + "name"]
            mask = state >> i
            value = mask & 0 
            storagehandler.save("boat." + in_name,value)
    print state



while True:
    # Read all i2c-modules from redis
    i2c_keys = r.keys("config.i2c.*")
    
    for key in i2c_keys:
        m = r.hgetall(key)           # get all modules for i2c
        if (m["active"] == "1"):     # only process when active
            sensor = m["type"]       # read sensor-type
            
            if sensor == "PCF8591":
                try:
                    readPCF8591(m)
                except:
                    pass
     
            if sensor == "LM75":
               try:
                   readLM75(m)
               except:
                   pass

            if sensor == "PCF8574_IN":
               try: 
                   readPCF8574_IN(m)
               except:
                   pass
    
            # if sensor unknown => just ignore
    time.sleep(10)
