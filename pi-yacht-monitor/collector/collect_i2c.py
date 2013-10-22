import storagehandler
import sys
import redis
from smbus import SMBus

r = redis.StrictRedis(host='localhost', port=6379, db=0)



def readHorterAnalogIn(config):
    print "Now reading HorterAnalogIn"
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = SMBus(busnumber)
    
    for i in range(0,4):
        port = "in" + str(i) + "-"

        in_active = config[port + "active"]
        if in_active == "1":
            print "port",port
            in_factor = float(config[port + "factor"])
            in_name   = config[port + "name"]
            
            value = int("0x0" + str(i),16)
            bus.write_byte(address,value)
            bus.read_byte(address)
            voltage_raw = bus.read_byte(address)
            print voltage_raw
            
            voltage = voltage_raw * in_factor
            storagehandler.save("boat." + name,voltage)


def readHorterTemp(config):
    print "Now reading HorterTemp"
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    name = config["name"]
    bus = SMBus(busnumber)
    temp_raw = bus.read_word(address)
    temp = 37 # replace with magic calculations
    storagehandler.save("boat." + name,temp)


i2c_keys = r.keys("config.i2c.*")

for key in i2c_keys:
    m = r.hgetall(key)
    if (m["active"] == "1"):
        sensor = m["type"]
        if sensor == "horter-analog-in":
            readHorterAnalogIn(m)
 

        if sensor == "horter-temp":
           readHorterTemp(m)


