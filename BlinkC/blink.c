// blink.c
// BlinkC
//
// Description:
// C program to blink an LED on a Raspberry Pi with the WiringPi library.
//
// Created by John Woolsey on 05/30/2018.
// Copyright © 2018 Woolsey Workshop.  All rights reserved.


// Includes
#include <signal.h>
#include <stdio.h>
#include <wiringPi.h>


// Pin Definitions
const int redLED = 29;  // WiringPi pin 29 (BCM pin 21, physical pin 40)


// Global Variables
volatile sig_atomic_t signal_received = 0;  // signal interrupt received


// Signal Interrupt Handler
void sigint_handler(int signal) {
   signal_received = signal;  // capture interrupt signal
}


// Main
int main(void) {
   // Detect when CRTL-C is pressed
   signal(SIGINT, sigint_handler);  // enable interrupt handler

   // Initialize WiringPi library
   // (program will terminate if an error is encountered)
   wiringPiSetup();

   // Pin setup
   pinMode(redLED, OUTPUT);  // set redLED pin as an output

   // Blink LED
   printf("Press CTRL-C to exit.\n");
   while (!signal_received) {      // runs until CTRL-C is pressed
      digitalWrite(redLED, HIGH);  // turn on LED
      delay(500);                  // wait 500 milliseconds
      digitalWrite(redLED, LOW);   // turn off LED
      delay(500);                  // wait 500 milliseconds
   }

   // Exit cleanly when CTRL+C is pressed
   pinMode(redLED, INPUT);  // reset redLED pin as an input
   printf("\nCompleted cleanup of GPIO resources.\n");
   return(signal_received);
}
