import RPi.GPIO as GPIO
from time import sleep
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
servo1 = GPIO.PWM(36,50)

servo1.start(0)
servo1.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(0)

xState = 0

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_left(self, value):
        global xState
        if -value <= (32767/2) and xState != -1:
            servo1.ChangeDutyCycle(9.5)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState=-1
        if -value > (32767/2) and xState != -2:
            servo1.ChangeDutyCycle(12)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState=-2
        

    def on_L3_right(self, value):
        global xState
        if value <= (32767/2) and xState != 1:
            servo1.ChangeDutyCycle(4.5)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState=1
        if value > (32767/2) and xState != 2:
            servo1.ChangeDutyCycle(2)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState=2

    def on_L3_x_at_rest(self):
        global xState
        servo1.ChangeDutyCycle(7)
        sleep(0.3)
        servo1.ChangeDutyCycle(0)
        xState = 0

    def on_circle_press(self):
        servo1.ChangeDutyCycle(7)
        sleep(0.5)
        servo1.ChangeDutyCycle(0)
        servo1.stop()
        GPIO.cleanup()
        quit()

try:
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=60)
except:
    print("Error")
    servo1.stop()
    GPIO.cleanup()
    quit()