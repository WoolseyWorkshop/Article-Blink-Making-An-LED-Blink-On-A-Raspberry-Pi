# blink_rpigpio.py
#
# Description:
# A Python program that blinks an LED on a Raspberry Pi using the RPi.GPIO
# library.
#
# Circuit:
# An LED is connected to BCM pin 21, physical pin 40.
#
# Created by John Woolsey on 05/30/2018.
# Modified by John Woolsey on 11/22/2022.
# Copyright (c) 2018 Woolsey Workshop.  All rights reserved.


# Imports
from time import sleep
import RPi.GPIO as GPIO


# Pin Mapping
RED_LED = 21


# Pin Configuration
GPIO.setmode(GPIO.BCM)         # use BCM pin numbering
GPIO.setup(RED_LED, GPIO.OUT)  # set RED_LED pin as an output


# Blink LED
print("Press CTRL-C to exit.")
try:
    while True:                          # runs forever
        GPIO.output(RED_LED, GPIO.HIGH)  # turn on LED
        sleep(1)                         # wait a second
        GPIO.output(RED_LED, GPIO.LOW)   # turn off LED
        sleep(1)                         # wait a second
finally:  # Exit cleanly when CTRL-C is pressed
    GPIO.cleanup()  # release all GPIO resources
