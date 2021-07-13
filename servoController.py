import turret2
import RPi.GPIO as GPIO
from time import sleep

print("cum1")
if turret2.controller.on_R2_press:
    print('cum')
