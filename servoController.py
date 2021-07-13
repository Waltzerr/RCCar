import turret2
import RPi.GPIO as GPIO
from time import sleep

turret2.start()
while turret2.quit != True:
    print("cum")
