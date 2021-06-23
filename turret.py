import RPi.GPIO as GPIO
from time import sleep
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
servo1 = GPIO.PWM(36,50)

servo1.start(0)
servo1.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(0)

angle = 0
degrees = float(input("Enter degrees to turn servo by: "))

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_left_arrow_press(self):
        global angle
        global degrees
        print(angle)
        if angle < 180:
            angle+=degrees
            servo1.ChangeDutyCycle(2+(angle/18))

    def on_right_arrow_press(self):
        global angle
        global degrees
        print(angle)
        if angle > 0:
            angle-=degrees
            servo1.ChangeDutyCycle(2+(angle/18))

    def on_left_right_arrow_release(self):
        servo1.ChangeDutyCycle(0)

    def on_circle_press(self):
        servo1.ChangeDutyCycle(2)
        servo1.stop()
        GPIO.cleanup()
        quit()

try:
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=60)
    if controller.on_left_arrow_press:
        print('cum')

except:
    print("Error")
    servo1.stop()
    GPIO.cleanup()
    quit()