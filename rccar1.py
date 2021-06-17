import RPi.GPIO as GPIO
import readchar
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while True:
  input=""
  input=readchar.readkey()
  GPIO.output(16, GPIO.LOW)
  if input=="w":
    GPIO.output(16, GPIO.HIGH) #forwards
    
  if input=="s":
    GPIO.output(18, GPIO.HIGH) #backwards
    
  if input=="a":
    GPIO.output(11, GPIO.HIGH) #left
    
  if input=="d":
    GPIO.output(13, GPIO.HIGH) #right
    
  if input=="q":
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
