import RPi.GPIO as GPIO
import pynput
from pynput.keyboard import Listener
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
  
def on_press(key):
    print("Key pressed: {0}".format(key))

def on_release(key):
    print("Key released: {0}".format(key))
    
with Listener(on_press=on_press, on_release=on_release) as listener:  # Create an instance of Listener
    listener.join()  # Join the listener thread to the main thread to keep waiting for keys

#GPIO.output(18, GPIO.HIGH) #backwards
#sleep(2)
#GPIO.output(18, GPIO.LOW)

#GPIO.output(13, GPIO.HIGH) #right
#sleep(2)
#GPIO.output(13, GPIO.LOW)

#GPIO.output(16, GPIO.HIGH) #forwards
#sleep(2)
#GPIO.output(16, GPIO.LOW)

#GPIO.output(11, GPIO.HIGH) #left
#sleep(2)
#GPIO.output(11, GPIO.LOW)

GPIO.cleanup()
