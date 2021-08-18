from motor import *
import keyboardController as kc

kc.init()

while True:
    lSpeed, rSpeed = kc.main()
    motor(lSpeed, rSpeed)