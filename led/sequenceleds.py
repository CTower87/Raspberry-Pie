#Lights truning on in sucsession

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

try:
    while 1:

        GPIO.output(27, GPIO.HIGH)# Blue on
        time.sleep(.1)
        
        GPIO.output(26, GPIO.HIGH)# Red on
        time.sleep(.1)
        
        GPIO.output(25, GPIO.HIGH)# Green on
        time.sleep(.1)
        
        GPIO.output(24, GPIO.HIGH)#yellow on
        time.sleep(.4)
        
        GPIO.output(24, GPIO.LOW)#all off
        GPIO.output(25, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        time.sleep(.1)

                    
except KeyboardInterrupt:
    GPIO.cleanup()
