# BlinkPython
Python programs that blink an LED on a Raspberry Pi using the RPi.GPIO and GPIO Zero libraries.

## Programs
[blink_rpigpio.py](blink_rpigpio.py) - Updates the LED pin directly within a simple loop using the RPi.GPIO library.

[blink_gpiozero_loop.py](blink_gpiozero_loop.py) - Uses the on() and off() methods of the the LED object defined in the GPIO Zero library within a simple loop.

[blink_gpiozero_blink.py](blink_gpiozero_blink.py) - Uses the blink() method of the the LED object defined in the GPIO Zero library.

## Run
$ python blink_rpigpio.py

$ python blink_gpiozero_loop.py

$ python blink_gpiozero_blink.py

## Exit
CTRL-C
