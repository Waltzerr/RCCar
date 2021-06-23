import RPi.GPIO as GPIO
from time import sleep
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
servo1 = GPIO.PWM(36,50)

servo1.start(0)
servo1.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(0)


class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_left(self, value):
        angle = int((2+((-1*value)/182)/18))
        servo1.ChangeDutyCycle(angle)
        print(angle)

    def on_L3_right(self, value):
        angle = int((2+(value/182)/18))
        servo1.ChangeDutyCycle(angle)
        print(angle)

    def on_L3_x_at_rest(self):
        servo1.ChangeDutyCycle(5)
        servo1.ChangeDutyCycle(0)

    def on_circle_press(self):
        servo1.ChangeDutyCycle(2)
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