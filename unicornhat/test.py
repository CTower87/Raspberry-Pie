import unicornhat as uc
import time


uc.brightness(.5)
uc.rotation(180)

x = 0
Y = 0

try:
    while 1:

        uc.set_pixel(x,Y,128,0,0)
        uc.set_pixel(x-1,Y,0,0,0)
        uc.show()
        time.sleep(.3)

        if x < 8:
            x = (x + 1)
        elif x == 8:
            x = 0
            uc.off()



except KeyboardInterrupt:
    uc.off()
