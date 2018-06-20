// main.swift
// BlinkSwift
//
// Description:
// Swift program to blink an LED on a Raspberry Pi with the SwiftyGPIO library.
//
// Created by John Woolsey on 06/15/2018.
// Copyright © 2018 Woolsey Workshop.  All rights reserved.


// Imports
import Foundation
import SwiftyGPIO


// Global Variables
var signalReceived: sig_atomic_t = 0  // signal interrupt received


// Pin Setup
let gpio = SwiftyGPIO.GPIOs(for: .RaspberryPi3)  // initialize SwiftyGPIO library for use with the Raspberry Pi
guard let redLED = gpio[GPIOName.P21] else {  // # BCM pin 21, physical pin 40
   fatalError("Could not initialize redLED.")
}
redLED.direction = .OUT  // set redLED pin as an output


// Signal Interrupt Handler
signal(SIGINT) { signal in
   signalReceived = signal  // capture interrupt signal
}


// Blink LED
print("Press CTRL-C to exit.")
while signalReceived == 0 {  // runs until CTRL-C is pressed
   redLED.value = 1          // turn on LED
   usleep(500000)            // wait 500,000 microseconds
   redLED.value = 0          // turn off LED
   usleep(500000)            // wait 500,000 microseconds
}

// Exit cleanly when CTRL+C is pressed
redLED.direction = .IN  // reset redLED pin as an input
print("\nCompleted cleanup of GPIO resources.")
exit(signalReceived)
