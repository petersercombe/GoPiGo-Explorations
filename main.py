from motor import *
from time import sleep

# go in a straight line for 2 seconds.
motor()
sleep(2)
gpg.stop()

# spin right for 2 seconds
motor(0, 1)
sleep(2)
gpg.stop()

# spin left for 2 seconds
motor(0, -1)
sleep(2)
gpg.stop()

# go in a straight line backwards for 2 seconds.
motor(-0.5, 0)
sleep(2)
gpg.stop()