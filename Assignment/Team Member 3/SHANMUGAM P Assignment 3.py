#python code for blinking LED and traffic lights for Raspberry pi
#python code for blinking LED

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low
(off)
while True: # Run forever
GPIO.output(8, GPIO.HIGH) # Turn on
sleep(1) # Sleep for 1 second
GPIO.output(8, GPIO.LOW) # Turn off
sleep(1) # Sleep for 1 second

#Python code for Traffic Light

import RPi.GPIO as GPIO
import time
import signal
import sys
# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
 GPIO.output(9, False)
 GPIO.output(10, False)
 GPIO.output(11, False)
 GPIO.cleanup()
 sys.exit(0)
signal.signal(signal.SIGINT, allLightsOff)
# Loop forever
while True:
 # Red
 GPIO.output(9, True)
 time.sleep(3)
 # Red and amber
 GPIO.output(10, True)
 time.sleep(1)
 # Green
 GPIO.output(9, False)
 GPIO.output(10, False)
 GPIO.output(11, True)
 time.sleep(5)
 # Amber
 GPIO.output(11, False)
 GPIO.output(10, True)
 time.sleep(2)
 # Amber off (red comes on at top of loop)
 GPIO.output(10, False)
Footer
© 2022 GitHub, Inc.
