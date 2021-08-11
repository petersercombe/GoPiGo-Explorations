from motor import *
from time import sleep

# Delay start of program so you can disconnect peripherals and place on ground
sleep(15)

sensor_readings = None
servo = gpg.init_servo('SERVO1')
dist = gpg.init_distance_sensor('I2C')
sleep(0.1)

# start
servo.rotate_servo(90)
while dist.read() > 5:
    motor()

gpg.stop()