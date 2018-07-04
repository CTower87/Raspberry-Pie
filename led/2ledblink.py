#two leds blinking at different intervals

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

Y = 0
R = 0

try:
    while 1:

        if Y == 5:
            GPIO.output(18, GPIO.HIGH)

        elif Y == 8:
            GPIO.output(18, GPIO.LOW)
            Y =  0

        if R == 7:
            GPIO.output(19, GPIO.HIGH)
            print(1)

        elif R == 10:
            GPIO.output(19, GPIO.LOW)
            R = 0
            print(2)

        Y = (Y + 1)
        R = (R + 1)
        time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
        
