#!/usr/bin/python
import storagehandler
import sys
import redis
from smbus import SMBus
import time
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('/var/log/i2ccollect.log')
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info('Hello baby')



r = redis.StrictRedis(host='localhost', port=6379, db=0)




# reads data from horter-analog-in-card
# converts it with factor to human-readable voltage
# save in redis with name from config
def readPCF8591(config):
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = SMBus(busnumber)
    logger.debug('Now reading HorterAnalogIn')
    logger.debug('Busnumber: ')
    logger.debug('Address: ')

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
    logger.debug('--------------------')
    logger.debug('Now reading LM75')
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    name = config["name"]
    bus = SMBus(busnumber)
    logger.debug('Busnumber: %s', busnumber)
    logger.debug('Address: %s', address)
    logger.debug('Name: %s', name)
    raw_temp = bus.read_word(address)
    vorkomma = raw_temp & 0xFF
    nachkomma = raw_temp >> 15
    temp = 0
    if (vorkomma & 0x80) != 0x80:
        temp = vorkomma + nachkomma * 0.5
    else:
        vorkomma = -((~vorkomma & 0xFF) + 1)
        temp = vorkomma + nachkomma * 0.5
    logger.debug('Temperatur: %s', temp)
    storagehandler.save("boat." + name,temp)


def readPCF8574_IN(config):
    logger('Now reading DigitalIn')
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = SMBus(busnumber)
    state = bus.read_byte(address)
    for i in range(0,8):
        port = "in" + str(i) + "-"
        in_active = config[port + "active"]
        if in_active == "1":
            in_name = config[port + "name"]
            value = 1&(state>>i)
            storagehandler.save("boat." + in_name,value)


def readPCF8574_OUT(config):
    logger.debug('Now reading DigitalOut')
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = SMBus(busnumber)
    state = bus.read_byte(address)
    for i in range(0,8):
        port = "in" + str(i) + "-"
        in_active = config[port + "active"]
        if in_active == "1":
            in_name = config[port + "name"]
            value = 1&(state>>i)
            value = 0 if value==1 else 1
            storagehandler.save("boat." + in_name,value)

logger.info('Start reading')

while True:
    # Read all i2c-modules from redis
    i2c_keys = r.keys("config.i2c.*")

    for key in i2c_keys:
        m = r.hgetall(key)           # get all modules for i2c
        if (m["active"] == "1"):     # only process when active
            sensor = m["type"]       # read sensor-type
            logging.debug('sensor ',sensor)

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

            if sensor == "PCF8574_OUT":
               try:
                  readPCF8574_OUT(m)
               except:
                  pass
            # if sensor unknown => just ignore

    time.sleep(10)
