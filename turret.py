import RPi.GPIO as GPIO
from time import sleep
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
servo1 = GPIO.PWM(36,50)

servo1.start(0)
servo1.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(0)

left = False
right = False

# try booleans and a loop
class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_left(self, value):
        global left, right
        right = False
        left = True

    def on_L3_right(self, value):
        global right, left
        left = False
        right = True

    def on_L3_x_at_rest(self):
        global left, right
        left = False
        right = False

    def on_circle_press(self):
        servo1.ChangeDutyCycle(2)
        sleep(0.5)
        servo1.stop()
        GPIO.cleanup()
        quit()

try:
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=60)
    while True:
        if left:
            print('left')
        if right:
           print('right')
except:
    print("Error")
    servo1.stop()
    GPIO.cleanup()
    quit()