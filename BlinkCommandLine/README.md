# BlinkCommandLine
Blink An LED On A Raspberry Pi With The gpio Command Line Utility

## Install:
% sudo apt-get install wiringpi

## View Help:
% gpio -h

## View Pinouts:
% gpio readall

## Set Pin Mode:
% gpio mode 29 out

## Turn On LED:
% gpio write 29 1

## Turn Off LED:
% gpio write 29 0

## Reset LED Resource
% gpio mode 29 in
