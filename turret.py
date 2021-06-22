import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
servo1 = GPIO.PWM(36,50)

servo1.start(0)
sleep(2)

duty = 2

while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    sleep(0.3)
    servo1.ChangeDutyCycle(0)
    sleep(0.7)
    duty += 1

sleep(2)

servo1.ChangeDutyCycle(7)
sleep(0.5)
servo1.ChangeDutyCycle(0)
sleep(1.5)

servo1.ChangeDutyCycle(2)
sleep(0.5)
servo1.ChangeDutyCycle(0)

servo1.stop()
GPIO.cleanup()