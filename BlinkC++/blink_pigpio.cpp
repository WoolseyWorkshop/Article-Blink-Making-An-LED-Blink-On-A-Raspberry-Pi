// blink_pigpio.cpp
//
// Description:
// A C++ program that blinks an LED on a Raspberry Pi using the pigpio library.
//
// Circuit:
// An LED is connected to BCM pin 21, physical pin 40.
//
// Created by John Woolsey on 10/12/2022.
// Modified by John Woolsey on 11/22/2022.
// Copyright (c) 2022 Woolsey Workshop.  All rights reserved.


// Includes
#include <csignal>
#include <iostream>
#include <pigpio.h>


// Pin Mapping
const int RedLED = 21;


// Global Variables
volatile sig_atomic_t signal_received = 0;  // interrupt signal received


// Signal Interrupt Handler
void sigint_handler(int signal) {
   signal_received = signal;  // capture interrupt signal
}


// Main
int main() {
   // Initialize pigpio library GPIO interface
   if (gpioInitialise() == PI_INIT_FAILED) {
      std::cout << "ERROR: Failed to initialize the GPIO interface." << std::endl;
      return 1;  // exit with positive number to denote failure
   }

   // Pin configuration
   gpioSetMode(RedLED, PI_OUTPUT);  // set RedLED pin as an output

   // Detect when CTRL-C is pressed
   signal(SIGINT, sigint_handler);  // enable interrupt handler

   // Blink LED
   std::cout << "Press CTRL-C to exit." << std::endl;
   while (!signal_received) {      // loops until CTRL-C is pressed
      gpioWrite(RedLED, PI_HIGH);  // turn on LED
      time_sleep(1);               // wait a second
      gpioWrite(RedLED, PI_LOW);   // turn off LED
      time_sleep(1);               // wait a second
   }

   // Exit cleanly when CTRL-C is pressed
   gpioSetMode(RedLED, PI_INPUT);  // reset RedLED pin as an input
   gpioTerminate();  // terminate pigpio library GPIO interface
   std::cout << std::endl;
   return 0;  // exit with zero to denote success
}
