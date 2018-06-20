# blink_gpiozero.py
# BlinkPython
#
# Description:
# Python program to blink an LED on a Raspberry Pi with the GPIO Zero library.
#
# Created by John Woolsey on 06/07/2018.
# Copyright c 2018 Woolsey Workshop.  All rights reserved.


# Imports
from gpiozero import LED
from time import sleep


# Pin Definitions
redLED = LED(21)  # BCM pin 21, physical pin 40


# Blink LED
print "Press CTRL-C to exit."
try:
   while True:      # runs forever
      redLED.on()   # turn on LED
      sleep(0.5)    # wait half a second
      redLED.off()  # turn off LED
      sleep(0.5)    # wait half a second


# Cleanup
finally:           # exit cleanly when CTRL+C is pressed
   redLED.close()  # release redLED resource
   print "\nCompleted cleanup of GPIO resources."
