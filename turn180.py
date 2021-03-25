import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
servo1.start(0)
print ("Moving servo!")
servo1.ChangeDutyCycle(9)
time.sleep(1.5)
servo1.ChangeDutyCycle(11)
time.sleep(0.5)
servo1.stop()
GPIO.cleanup()
