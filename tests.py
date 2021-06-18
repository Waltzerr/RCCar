import RPi.GPIO as GPIO
import readchar
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while True:
    input=readchar.readkey()
    chan_list = []
  
    if input=="w":
        chan_list.append(16)

    if input=="e":
        chan_list.append(16)
        chan_list.append(13)

    if input=="q":
        chan_list.append(16)
        chan_list.append(11)
    
    if input=="s":
        chan_list.append(18)

    if input=="d":
        chan_list.append(18)
        chan_list.append(13)

    if input=="a":
        chan_list.append(18)
        chan_list.append(11)
    
    if input=="r":
        break

    GPIO.output(tuple(chan_list), GPIO.HIGH)
    print(f"GPIO outs: {chan_list}")
    sleep(0.45)
    GPIO.output(tuple(chan_list), GPIO.LOW)
  

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
