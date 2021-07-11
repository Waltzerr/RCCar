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
maxValue = 32767

def getState(value):
        global maxValue
        for div in range(1,6):
            if value <= div*(maxValue/5):
                return div

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_R3_left(self, value):
        global xState
        state = getState(-value)
        if -state != xState:
            print(f"{state}, {xState}")
            servo1.ChangeDutyCycle(state+7)
            sleep(0.05)
            servo1.ChangeDutyCycle(0)
            xState=-state
        print(f"Value: {value}, State: {xState}")
        

    def on_R3_right(self, value):
        global xState
        state = getState(value)
        if state != xState:
            print(f"{state}, {xState}")
            servo1.ChangeDutyCycle(7-state)
            sleep(0.05)
            servo1.ChangeDutyCycle(0)
            xState=state
        print(f"Value: {value}, State: {xState}")

    def on_R3_x_at_rest(self):
        global xState
        servo1.ChangeDutyCycle(7)
        sleep(0.2)
        servo1.ChangeDutyCycle(0)
        xState = 0

    def on_R3_up(self, value):
        global yState
        state = getState(-value)
        if -state != yState:
            print(f"{state}, {yState}")
            servo2.ChangeDutyCycle(7-state)
            sleep(0.05)
            servo2.ChangeDutyCycle(0)
            yState=-state
        print(f"Value: {value}, State: {yState}")
        

    def on_R3_down(self, value):
        global yState
        state = getState(value)
        if state != yState:
            print(f"{state}, {yState}")
            servo2.ChangeDutyCycle(state+7)
            sleep(0.05)
            servo2.ChangeDutyCycle(0)
            yState=state
        print(f"Value: {value}, State: {yState}")

    def on_R3_y_at_rest(self):
        global yState
        servo2.ChangeDutyCycle(7)
        sleep(0.2)
        servo2.ChangeDutyCycle(0)
        yState = 0

    def on_circle_press(self):
        servo1.ChangeDutyCycle(7)
        sleep(0.25)
        servo1.ChangeDutyCycle(0)
        quit()

    def on_R2_press(self, value):
       GPIO.output(29, GPIO.HIGH)

    def on_R2_release(self):
       GPIO.output(29, GPIO.LOW)

    def on_R1_press(self, value):
        if GPIO.output(29):
            GPIO.output(29, GPIO.HIGH)
        else:
            GPIO.output(29, GPIO.LOW)


try:
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=60)
except:
    servo1.stop()
    GPIO.cleanup()
    print("Turret disconnected")
    quit()