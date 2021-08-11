# Import required modules
import time
from easygopigo3 import EasyGoPiGo3

# Initiating the GoPiGo object
gpg = EasyGoPiGo3()

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
    gpg.steer(lSpeed, rSpeed)