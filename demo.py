
import os
import RPi.GPIO as gpio

import REDLed as RED
import LED, random
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# BUTTON PINOUT
BT1=27
BT2=22

gpio.setup(BT1,gpio.IN)
gpio.setup(BT2,gpio.IN)

def Parla(msg):
	os.system('espeak "%s" -v it'%msg)

print "PREMI UN PULSANTE PER ACCENDERE O SPEGNERE I LED"
RED.ON()

leds = 6

while True:
	if gpio.input(BT1) == False:
		Parla("Operazione avviata")
		LED.ALL(False)
		led = random.randint(1,5)
		print led
		if led == 1:
			LED.LED1(True)
		elif led == 2:
			LED.LED2(True)
		elif led == 3:
			LED.LED3(True)
		elif led == 4:
			LED.LED4(True)
		elif led == 5:
			LED.LED5(True)
		elif led == 0:
			LED.ALL(False)
		
	elif gpio.input(BT2) == False:
		LED.ALL(True,2)
		sleep(0.5)
		RED.SCALE(False,0.3)
		sleep(.1)
		RED.ON()
		sleep(.5)
		RED.OFF()
		sleep(.5)
		RED.ON()
		sleep(.5)
		RED.OFF()
		sleep(.5)
		RED.ON()
		sleep(.5)
		RED.OFF()
		sleep(.5)
		RED.SCALE(True,0.2)