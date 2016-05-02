from smbus import SMBus
from time import sleep
import math, csv

bus = SMBus(1)

addr = 0x48
chan = 0x40

# Spengo il red rosso
bus.write_byte_data(addr,chan, 0)
sleep(.3)

def ON(value=255):
        bus.write_byte_data(addr,chan, value)
def OFF():
        bus.write_byte_data(addr,chan, 0)
		
def SCALE(state=False,timeout=0.5):
	if state == True:
		for n in range(256):
			bus.write_byte_data(addr,chan, n)
			sleep(timeout)
	elif state == False:
		for n in reversed(range(255)):
			bus.write_byte_data(addr,chan, n)
			sleep(timeout)