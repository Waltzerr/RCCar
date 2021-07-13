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

stateAdj = 0.5
xState = 7
yState = 7
maxValue = 32767

def getState(value):
        global maxValue
        for div in range(1,6):
            if value <= div*(maxValue/5):
                return div

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_left_arrow_press(self):
        global xState
        if xState < 12:
            xState += stateAdj
            servo1.ChangeDutyCycle(xState)
            sleep(0.05)
            servo1.ChangeDutyCycle(0)

    def on_right_arrow_press(self):
        global xState
        if xState > 1:
            xState += -stateAdj
            servo1.ChangeDutyCycle(xState)
            sleep(0.05)
            servo1.ChangeDutyCycle(0)

    def on_down_arrow_press(self):
        global yState
        if yState < 12:
            yState += stateAdj
            servo2.ChangeDutyCycle(yState)
            sleep(0.05)
            servo2.ChangeDutyCycle(0)

    def on_up_arrow_press(self):
        global yState
        if yState > 1:
            yState += -stateAdj
            servo2.ChangeDutyCycle(yState)
            sleep(0.05)
            servo2.ChangeDutyCycle(0)

    def on_circle_press(self):
        servo1.ChangeDutyCycle(7)
        sleep(0.25)
        servo1.ChangeDutyCycle(0)
        quit()

    def on_R2_press(self, value):
       GPIO.output(29, GPIO.HIGH)

    def on_R2_release(self):
       GPIO.output(29, GPIO.LOW)

try:
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=60)
except:
    servo1.stop()
    GPIO.cleanup()
    print("Turret disconnected")
    quit()