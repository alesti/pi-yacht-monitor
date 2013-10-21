#/usr/bin/python

import commands
from time import sleep
cmd= 'i2cget -y 1 0x48 00x00 w'

def calcTemp(wert):
	vorkomma = wert & 0xFF
	nachkomma = wert >> 15
	# ist Wert positiv oder negativ
	if (vorkomma & 0x80)!= 0x80: #positiv
		temp = vorkomma + nachkomma * 0.5
	else: #negativ
		vorkomma =-((~vorkomma & 0xFF) +1)
		temp = vorkomma + nachkomma *(0.5)
	print str(temp) + ' Grad Celsius'

def main():
	go = True
while go:
	try:
		status, output = commands.getstatusoutput(cmd)
                #Ergebnis ist ein Tuble
if status == 0:
			calcTemp(int(output,16))
			sleep(1)
		else:
			print 'Fehler!'
			print output
			go = False
		exept KeyboardInterrupt:
			go = False
if __name__ == '__main__':
	main()
