"""my cool lights"""

import random
import RPi.GPIO as GPIO
import time as t

pins  = [4,27,22,5,6,13,19,26]
default_speed= .1


GPIO.setmode(GPIO.BCM)
GPIO.setup(pins,GPIO.OUT)

def on(pin): GPIO.output(pin,GPIO.HIGH)

def off(pin): GPIO.output(pin,GPIO.LOW)

def slowon(list=pins,delay=1):
    for pin in list:
        on(pin)
        t.sleep(delay)

def slowoff(list=pins,delay=1):
    for pin in list:
        off(pin)
        t.sleep(delay)

def chase(count=1,delay=default_speed):
    for n in range(count):
        slowon(delay=delay)
        slowoff(delay=delay)

def updown(count=1,delay=.1):
    for n in range(count):
        slowon(delay=delay)
        slowoff(delay=delay,list=pins[::-1])


patterns = [chase,updown]


if __name__ == "__main__":
    choices = [slowon(),chase(),updown(),slowoff()]
    while True:
        random.choice(choices)

