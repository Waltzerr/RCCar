import RPi.GPIO as GPIO
from time import sleep
from pyPS4Controller.controller import Controller

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
servo1 = GPIO.PWM(36,50)

servo1.start(0)
servo1.ChangeDutyCycle(0)

duty = 0

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_left(self, value):
        global duty
        if duty<12:
            duty += 1
        servo1.ChangeDutyCycle(duty)
        print(f"Duty: {duty}")

    def on_L3_right(self, value):
        global duty
        if duty>1:
            duty += -1
        servo1.ChangeDutyCycle(duty)
        print(f"Duty: {duty}")

    def on_L3_x_at_rest(self):
        servo1.ChangeDutyCycle(0)

    def on_circle_press(self):
        servo1.stop()
        GPIO.cleanup()
        quit()

try:
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    # you can start listening before controller is paired, as long as you pair it within the timeout window
    controller.listen(timeout=60)
except:
    print("Error")
    servo1.stop()
    GPIO.cleanup()
    quit()


# try:
#     while True:
#         angle = float(input('Enter angle between 0 and 180: '))
#         servo1.ChangeDutyCycle(2+(angle/18))
#         sleep(0.5)
#         servo1.ChangeDutyCycle(0)

# finally:
#     servo1.stop()
#     GPIO.cleanup()

# sleep(2)

# duty = 2

# while duty <= 12:
#     servo1.ChangeDutyCycle(duty)
#     sleep(0.3)
#     servo1.ChangeDutyCycle(0)
#     sleep(0.7)
#     duty += 1

# sleep(2)

# servo1.ChangeDutyCycle(7)
# sleep(0.5)
# servo1.ChangeDutyCycle(0)
# sleep(1.5)

# servo1.ChangeDutyCycle(2)
# sleep(0.5)
# servo1.ChangeDutyCycle(0)