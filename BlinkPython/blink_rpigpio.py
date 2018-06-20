# blink_rpigpio.py
# BlinkPython
#
# Description:
# Python program to blink an LED on a Raspberry Pi with the RPi.GPIO library.
#
# Created by John Woolsey on 05/30/2018.
# Copyright c 2018 Woolsey Workshop.  All rights reserved.


# Imports
import RPi.GPIO as GPIO
import time


# Pin Definitions
redLED = 21  # BCM pin 21, physical pin 40


# Pin Setup
GPIO.setmode(GPIO.BCM)        # use BCM pin numbering
GPIO.setup(redLED, GPIO.OUT)  # set redLED pin as an output


# Blink LED
print "Press CTRL-C to exit."
try:
   while True:                        # runs forever
      GPIO.output(redLED, GPIO.HIGH)  # turn on LED
      time.sleep(0.5)                 # wait half a second
      GPIO.output(redLED, GPIO.LOW)   # turn off LED
      time.sleep(0.5)                 # wait half a second


# Cleanup
finally:           # exit cleanly when CTRL+C is pressed
   GPIO.cleanup()  # release all GPIO resources
   print "\nCompleted cleanup of GPIO resources."
