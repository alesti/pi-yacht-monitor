#/usr/bin/python

 ##########################################
 # Funktion zum Auslesen des Temp-Sensors
 ##########################################

 # Da ich ja immernoch kein Datenmodell habe
 # Bitte REDIS anpassen !!!
 #
 # Benutze Werte :
 #
 # HSET "config.sensor.1" "ID" "1"
 # HSET "config.sensor.1" "Typ" "i2c"
 # HSET "config.sensor.1" "Address" "0x48"
 # HSET "config.sensor.1" "Active" "true"
 #
 # HSET "boat.temperature" "value" "20.0"
 # HSET "boat.temperature" "time" "Thu Oct 31 19:15:40 2013"

from smbus import SMBus
import redis
import time
r_server = redis.Redis("localhost")
vtime = time.ctime()

def getTemp():
       rdis_addr = r_server.hget("config.sensor.1", "Address")
       address = int(rdis_addr,16)
       bus = SMBus(1)

       raw_temp = bus.read_byte(address);

       vorkomma = raw_temp & 0xFF
       nachkomma = raw_temp >> 15

        # ist Wert positiv oder negativ
       if (vorkomma & 0x80)!= 0x80: #positiv
                temp = vorkomma + nachkomma * 0.5
       else: #negativ
                vorkomma =-((~vorkomma & 0xFF) +1)
                temp = vorkomma + nachkomma *(0.5)

       #print (temp)
       r_server.hset("boat.temperature","value",temp)
       r_server.hset("boat.temperature","time", vtime)
 #########################################

 # Hauptprogramm
getTemp()
