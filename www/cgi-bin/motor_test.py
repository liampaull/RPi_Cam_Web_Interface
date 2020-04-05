#!/usr/bin/python3

import cgitb
cgitb.enable()
print ("Content-type: text/html\n")
print ("Hello World!")

"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit

kit = MotorKit()

for i in range(1000):
        kit.stepper1.onestep()


kit.stepper1.release()
