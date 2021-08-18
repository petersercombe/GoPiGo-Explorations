from motor import *
import keyboardController as kc

kc.init()

while True:
    throttle, steering = kc.main()
    motor(throttle, steering)
    # Capture image from camera
    # Save throttle/steering values with image