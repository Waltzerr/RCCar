import RPi.GPIO as GPIO
from time import sleep
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
servo1 = GPIO.PWM(36,50)
GPIO.setup(32, GPIO.OUT)
servo2 = GPIO.PWM(32,50)
GPIO.setup(29, GPIO.OUT)

servo1.start(0)
servo1.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(0)
servo2.start(0)
servo2.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(0)

xState = 0
yState = 0

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_R3_left(self, value):
        global xState
        if -value <= (15384) and -value > 1500 and xState != -1:
            servo1.ChangeDutyCycle(9.5)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState=-1
            print(f"Value: {value}, X: {xState}")
        elif -value > (17384) and xState != -2:
            servo1.ChangeDutyCycle(12)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState=-2
            print(f"Value: {value}, X: {xState}")
        

    def on_R3_right(self, value):
        global xState
        if value <= (15384) and value > 1500 and xState != 1:
            servo1.ChangeDutyCycle(4.5)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState=1
            print(f"Value: {value}, X: {xState}")
        elif value > (17384) and xState != 2:
            servo1.ChangeDutyCycle(2)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState=2
            print(f"Value: {value}, X: {xState}")

    def on_R3_x_at_rest(self):
        global xState
        if xState != 0:
            servo1.ChangeDutyCycle(7)
            sleep(0.1)
            servo1.ChangeDutyCycle(0)
            xState = 0
            print(f"X: {xState}")

    def on_R3_down(self, value):
        global yState
        if value <= (15384) and value > 1500 and yState != -1:
            servo2.ChangeDutyCycle(9.5)
            sleep(0.1)
            servo2.ChangeDutyCycle(0)
            yState=-1
            print(f"Value: {value}, Y: {yState}")
        elif value > (17384) and yState != -2:
            servo2.ChangeDutyCycle(12)
            sleep(0.1)
            servo2.ChangeDutyCycle(0)
            yState=-2
            print(f"Value: {value}, Y: {yState}")
        

    def on_R3_up(self, value):
        global yState
        if -value <= (15384) and -value > 1500 and yState != 1:
            servo2.ChangeDutyCycle(4.5)
            sleep(0.1)
            servo2.ChangeDutyCycle(0)
            yState=1
            print(f"Value: {value}, Y: {yState}")
        elif -value > (17384) and yState != 2:
            servo2.ChangeDutyCycle(2)
            sleep(0.1)
            servo2.ChangeDutyCycle(0)
            yState=2
            print(f"Value: {value}, Y: {yState}")

    def on_R3_y_at_rest(self):
        global yState
        if yState != 0:
            servo2.ChangeDutyCycle(7)
            sleep(0.1)
            servo2.ChangeDutyCycle(0)
            yState = 0
            print(f"Y: {yState}")

    def on_circle_press(self):
        servo1.ChangeDutyCycle(7)
        sleep(0.5)
        quit()

    def on_R2_press(self, value):
       GPIO.output(29, GPIO.HIGH)

    def on_R2_release(self):
       GPIO.output(29, GPIO.LOW)

try:
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=60)
except:
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    servo1.ChangeDutyCycle(7)
    servo2.ChangeDutyCycle(7)
    servo2.stop()
    servo1.stop()
    GPIO.cleanup()
    print("Turret disconnected")
    quit()