"""my cool lights"""

import RPI.GPIO as GPIO
import time as t

pins  = [4,27,22,5,6,13,19,26]

GPIO.setmode(GPIO.BMC)
GPIO.setup(pins,GPIO.OUT)

def on(pin): GPIO.output(pin,GPIO.HIGH)

def off(pin): GPIO.output(pin,GPIO.LOW

def slowon(list=pins,delay=,1):
    for pin in list:
        on(pin)
        t.sleep(delay)

def slowoff(list=pins,delay=,1):
    for pin in list:
        off(pin)
        t.sleep(delay)

def chase(count=1):
    for n in range(count):
        slowon()
        slowoff()



