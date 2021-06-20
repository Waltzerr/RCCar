from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
       GPIO.output(16, GPIO.HIGH)

    def on_down_arrow_press(self):
       GPIO.output(18, GPIO.HIGH)

    def on_up_down_arrow_release(self):
       GPIO.output((16, 18), GPIO.LOW)

    def on_left_arrow_press(self):
       GPIO.output(11, GPIO.HIGH)

    def on_right_arrow_press(self):
       GPIO.output(13, GPIO.HIGH)

    def on_left_right_arrow_release(self):
       GPIO.output((11, 13), GPIO.LOW)
    
    def on_circle_press(self):
        GPIO.cleanup()
        quit()

try:
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    # you can start listening before controller is paired, as long as you pair it within the timeout window
    controller.listen(timeout=60)
except:
    print("Error connecting to controller")
    quit()
