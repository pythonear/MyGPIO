#! /usr/bin/python

from time import sleep
import RPi.GPIO as gpio


gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# LED PINOUT
LD1 = 4
LD2 = 25
LD3 = 24
LD4 = 23
LD5 = 18

gpio.setup(LD1, gpio.OUT)
gpio.setup(LD2, gpio.OUT)
gpio.setup(LD3, gpio.OUT)
gpio.setup(LD4, gpio.OUT)
gpio.setup(LD5, gpio.OUT)

# SPENGO TUTTI I LED 

gpio.output(LD1, False)
gpio.output(LD2, False)
gpio.output(LD3, False)
gpio.output(LD4, False)
gpio.output(LD5, False)

# Funzioni di controllo dei LED
def LED1(state=False):
	if state == False:
		gpio.output(LD1, False)
		sleep(.2)
	elif state == True:
		gpio.output(LD1, True)
		sleep(.2)
		
def LED2(state=False):
	if state == False:
		gpio.output(LD2, False)
		sleep(.2)
	elif state == True:
		gpio.output(LD2, True)
		sleep(.2)
		
def LED3(state=False):
	if state == False:
		gpio.output(LD3, False)
		sleep(.2)
	elif state == True:
		gpio.output(LD3, True)
		sleep(.2)
		
def LED4(state=False):
	if state == False:
		gpio.output(LD4, False)
		sleep(.2)
	elif state == True:
		gpio.output(LD4, True)
		sleep(.2)
		
def LED5(state=False):
	if state == False:
		gpio.output(LD5, False)
		sleep(.2)
	elif state == True:
		gpio.output(LD5, True)
		sleep(.2)
		
def ALL(state=False,timeout=0):
	if state == False:
		sleep(timeout)
		gpio.output(LD1, False)
		gpio.output(LD2, False)
		gpio.output(LD3, False)
		gpio.output(LD4, False)
		gpio.output(LD5, False)
	
	elif state == True:
		sleep(timeout)
		gpio.output(LD1, True)
		gpio.output(LD2, True)
		gpio.output(LD3, True)
		gpio.output(LD4, True)
		gpio.output(LD5, True)
	
def EFFECT(state,side='LEFT',timeout=0.2):
	if state == True:
		if side == 'LEFT':
			gpio.output(LD1, True)
			sleep(timeout)
			gpio.output(LD1, False)
			sleep(timeout)
			gpio.output(LD2, True)
			sleep(timeout)
			gpio.output(LD2, False)
			sleep(timeout)
			gpio.output(LD3, True)
			sleep(timeout)
			gpio.output(LD3, False)
			sleep(timeout)
			gpio.output(LD4, True)
			sleep(timeout)
			gpio.output(LD4, False)
			sleep(timeout)
			gpio.output(LD5, True)
			
		elif side == 'RIGHT':
			gpio.output(LD5, True)
			sleep(timeout)
			gpio.output(LD5, False)
			sleep(timeout)
			gpio.output(LD4, True)
			sleep(timeout)
			gpio.output(LD4, False)
			sleep(timeout)
			gpio.output(LD3, True)
			sleep(timeout)
			gpio.output(LD3, False)
			sleep(timeout)
			gpio.output(LD2, True)
			sleep(timeout)
			gpio.output(LD2, False)
			sleep(timeout)
			gpio.output(LD1, True)
			
	elif state == False:
		if side == 'LEFT':
			gpio.output(LD1, False)
			sleep(timeout)
			gpio.output(LD2, True)
			sleep(timeout)
			gpio.output(LD2, False)
			sleep(timeout)
			gpio.output(LD3, True)
			sleep(timeout)
			gpio.output(LD3, False)
			sleep(timeout)
			gpio.output(LD4, True)
			sleep(timeout)
			gpio.output(LD4, False)
			sleep(timeout)
			gpio.output(LD5, True)
			sleep(timeout)
			gpio.output(LD5, False)
			
		elif side == 'RIGHT':
			gpio.output(LD5, False)
			sleep(timeout)
			gpio.output(LD4, True)
			sleep(timeout)
			gpio.output(LD4, False)
			sleep(timeout)
			gpio.output(LD3, True)
			sleep(timeout)
			gpio.output(LD3, False)
			sleep(timeout)
			gpio.output(LD2, True)
			sleep(timeout)
			gpio.output(LD2, False)
			sleep(timeout)
			gpio.output(LD1, True)
			sleep(timeout)
			gpio.output(LD1, False)