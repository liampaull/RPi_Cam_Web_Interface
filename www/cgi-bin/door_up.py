#!/usr/bin/python3

print ("Content-Type: text/plain;charset=utf-8")
print ("")


from adafruit_motorkit import MotorKit
kit = MotorKit()
kit.motor1.throttle = 0.0
