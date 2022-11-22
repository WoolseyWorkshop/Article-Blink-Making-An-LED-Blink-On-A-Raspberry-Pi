# BlinkCommandLine
Blink an LED on a Raspberry Pi with the raspi-gpio command line utility.

## View Help
$ raspi-gpio help

## Read All GPIO Pins
$ raspi-gpio get

## Read A Single GPIO Pin (21)
$ raspi-gpio get 21

## Set A Single GPIO Pin (21) As An Input
$ raspi-gpio set 21 ip

## Set A Single GPIO Pin (21) As An Output
$ raspi-gpio set 21 op

## Drive A Single GPIO Pin (21) Low (Turn Off The LED)
$ raspi-gpio set 21 dl

## Drive A Single GPIO Pin (21) High (Turn On The LED)
$ raspi-gpio set 21 dh

## Reset The LED Resource (Set GPIO Pin 21 Back To An Input)
$ raspi-gpio set 21 ip
