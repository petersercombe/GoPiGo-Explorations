# -*- encoding: utf-8 -*-

import socket
import sys

# In USB connection mode, the default IP address of the robot is 192.168.42.2 and the control command port is port 40923.
host = "192.168.42.2"
port = 40923

from robomaster import robot

#initialise robot object
ep = robot.Robot()
ep.initialize()
chassis = ep.chassis

# set max speed
maxSpeed = 50

# Define a function to take throttle and steering input to control motors.
def motor(throttle=0.5, steering=0):
    # Set motor speeds. Can take values between -100 and 100
    lSpeed = (throttle + steering) * maxSpeed
    if lSpeed > maxSpeed: lSpeed = maxSpeed
    elif lSpeed < -maxSpeed: lSpeed = -maxSpeed

    rSpeed = (throttle - steering) * maxSpeed
    if rSpeed > maxSpeed: rSpeed = maxSpeed
    elif rSpeed < -maxSpeed: rSpeed = -maxSpeed

    # Control the speed of each motor individually
    chassis.drive_wheels(w1=lSpeed, w2=lSpeed, w3=rSpeed, w4=rSpeed)
    print(lSpeed, rSpeed)

ep.close()
