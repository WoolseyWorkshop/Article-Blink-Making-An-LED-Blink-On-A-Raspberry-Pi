# blink_gpiozero_loop.py
#
# Description:
# A Python program that blinks an LED on a Raspberry Pi using the GPIO Zero
# library.
#
# Circuit:
# An LED is connected to BCM pin 21, physical pin 40.
#
# Created by John Woolsey on 06/07/2018.
# Modified by John Woolsey on 11/22/2022.
# Copyright (c) 2018 Woolsey Workshop.  All rights reserved.


# Imports
from time import sleep
from gpiozero import LED


# Pin Mapping
red_led = LED(21)


# Blink LED
print("Press CTRL-C to exit.")
while True:        # runs forever
    red_led.on()   # turn on LED
    sleep(1)       # wait a second
    red_led.off()  # turn off LED
    sleep(1)       # wait a second
