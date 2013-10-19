# Lässt eine LED im als Parameter angegebenen
# Intervall blinken
#
# Das Script muss als User root ausgeführt
# werden.

#!/bin/bash

# Nur ausführen, wenn ein Intervall übergeben wurde
if [ $# -ne 1 ]; then
  echo "Usage: 002_blink.sh <interval>"
  exit 0
fi

# LED Zustand initialisieren
VALUE=0

# pin 25 exportieren
echo 25 > /sys/class/gpio/export

# Pin als Ausgang schalten
echo out > /sys/class/gpio/gpio25/direction

# Wenn Strg+C gedrückt wurde, LED ausschalten und Port wieder freigeben
trap 'echo "Exit, unexport pin25"; echo 0 > /sys/class/gpio/gpio25/value; echo 25 > /sys/class/gpio/unexport; exit 0' INT

# Hier wird geblinkt
while true
do
  echo $VALUE > /sys/class/gpio/gpio25/value
  sleep $1
  if [ $VALUE -eq 0 ]; then
    VALUE=1
  else
    VALUE=0
  fi
done

# Pin 25 wieder freigeben

echo 25 > /sys/class/gpio/unexport

