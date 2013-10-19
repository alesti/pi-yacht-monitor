# Schaltet eine LED an und nach kurzer Zeit 
# wieder aus, die an den GPIO-Pin 25 
# angeschlossen ist. 
#
# Das Script muss als User root ausgeführt
# werden.

#!/bin/bash

# pin 25 exportieren
echo 25 > /sys/class/gpio/export

# Pin als Ausgang schalten
echo out > /sys/class/gpio/gpio25/direction

# LED anschalten
echo 1 > /sys/class/gpio/gpio25/value

# 5 Sekunden warten
sleep 5

#LED wieder ausschalten
echo 0 > /sys/class/gpio/gpio25/value

# Pin 25 wieder freigeben
echo 25 > /sys/class/gpio/unexport


