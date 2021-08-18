#from motor import *
import keyboardController
from time import sleep

# Delay start of program so you can disconnect peripherals and place on ground
sleep(15)

# Initialise sensors and servos
sensor_readings = None
servo = gpg.init_servo('SERVO1')
dist = gpg.init_distance_sensor('I2C')
sleep(0.1)



def checkLeft():
    servo.rotate_servo(180)
    sleep(0.3)
    if dist.read() > 5:
        pass

def spin():
    motor(0,-1)
    sleep(0.5) #modify this so you get a 90 degree turn
    gpg.stop()
    servo.rotate_servo(90)

# start
#while True:
    #servo.rotate_servo(90)
#    if dist.read() > 5:
 #       motor()
  #  else:
   #     gpg.stop()
    #    checkLeft()

