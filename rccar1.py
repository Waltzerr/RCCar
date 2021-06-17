import RPi.GPIO as GPIO
import keyboard
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while True:
  try:
    if keyboard.is_pressed('w'):
            print("Going forward!")
            GPIO.output(16, GPIO.HIGH)
    else:
      GPIO.output(16, GPIO.LOW)
  except:
    break

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
