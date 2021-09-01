from motor import *
import keyboardController as kc
from time import sleep

kc.init()

while True:
    throttle, steering = kc.main()
    if throttle > 0 and dist.read() < 5:
        throttle = 0
    motor(throttle, steering)
    sleep(0.05)
    # Capture image from camera
    # Save throttle/steering values with image