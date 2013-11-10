#!/usr/bin/python
import storagehandler
import sys
import redis
import smbus
import time
import logging
import traceback


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

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# reads data from horter-analog-in-card
# converts it with factor to human-readable voltage
# save in redis with name from config
def readPCF8591(config):
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = smbus.SMBus(busnumber)
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
    bus = smbus.SMBus(busnumber)
    logger.debug('Busnumber: %s', busnumber)
    logger.debug('Address: %s', address)
    logger.debug('Name: %s', name)
    raw_temp = bus.read_word_data(address, 0)
    logger.debug('Raw Temp: %s', raw_temp)
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
    logger.debug('--------------------')
    logger.debug('Now reading DigitalIn')
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = smbus.SMBus(busnumber)
    state = bus.read_byte(address)
    for i in range(0,8):
        port = "in" + str(i) + "-"
        in_active = config[port + "active"]
        if in_active == "1":
            in_name = config[port + "name"]
            value = 1&(state>>i)
            storagehandler.save("boat." + in_name,value)


def readPCF8574_OUT(config):
    logger.debug('--------------------')
    logger.debug('Now reading DigitalOut')
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    logger.debug('Busnumber: %s', busnumber)
    logger.debug('Address: %s', address)
    bus = smbus.SMBus(busnumber)
    state = bus.read_byte(address);
    logger.debug('State: %s', state)

    for i in range(0,8):
        port = "in" + str(i) + "-"
        in_active = config[port + "active"]
        if in_active == "1":
            in_name = config[port + "name"]
            value = 1&(state>>7-i)
            logger.debug('In_Name: %s', in_name)
            logger.debug('Value: %s', value)
            storagehandler.save("boat." + in_name,value)

def readPCF8574_OUT_INV(config):
    logger.debug('--------------------')
    logger.debug('Now reading DigitalOut invers')
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    logger.debug('Busnumber: %s', busnumber)
    logger.debug('Address: %s', address)
    bus = smbus.SMBus(busnumber)
    state = bus.read_byte(address);
    logger.debug('State dez: %s', state)
    logger.debug('State bin: %s', bin(state))

    for i in range(0,8):
        port = "in" + str(i) + "-"
        in_active = config[port + "active"]
        if in_active == "1":
            in_name = config[port + "name"]
            value = 1&(state>>(7-i))
            value = 0 if value==1 else 1
            try:
                givenvalue=int(config[port + "givenvalue"])
            except:
                givenvalue=value
            if value != givenvalue:
                value = writePCF8574_OUT_INV(config,i,givenvalue)
                time.sleep(0.1)
            storagehandler.save("boat." + in_name,value)

def writePCF8574_OUT_INV(config,bit,givenvalue):
    address = int(config["address"],16)
    busnumber = int(config["bus"])
    bus = smbus.SMBus(busnumber)
    state = bus.read_byte(address)
    if givenvalue == 1:
        mask = 1 << (7-bit)
        mask = ~mask
        state = state & mask
        bus.write_byte(address,state)
        time.sleep(0.1)
    if givenvalue == 0:
        mask = 1<<(7-bit)
        state = state | mask
        bus.write_byte(address,state)
    state=bus.read_byte(address)
    value = 1&(state>>(7-bit))
    value = 0 if value==1 else 1
    return value



logger.info('****************************************')
logger.info('              Start reading')
logger.info('****************************************')

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
                   logger.error("Error while reading PCF8591") 

            if sensor == "LM75":
               try:
                   readLM75(m)
               except:
                   logger.error("Error while reading LM75")

            if sensor == "PCF8574_IN":
               try:
                   readPCF8574_IN(m)
               except:
                   logger.error("Error while reading PCF8574_IN")
                   traceback.print_exc(file=sys.stdout)

            if sensor == "PCF8574_OUT":
               try:
                  readPCF8574_OUT(m)
               except:
                  logger.error("Error while reading PCF8574_OUT")

            if sensor == "PCF8574_OUT_INV":
               try:
                  readPCF8574_OUT_INV(m)
               except:
                  logger.error("Error while reading PCF8574_OUT_INV")
            # if sensor unknown => just ignore

    time.sleep(5)
