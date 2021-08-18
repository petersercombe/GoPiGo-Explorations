from motor import *
import keyboardController as kc
from time import sleep

kc.init()

while True:
    throttle, steering = kc.main()
    motor(throttle, steering)
    sleep(0.05)
    # Capture image from camera
    # Save throttle/steering values with image