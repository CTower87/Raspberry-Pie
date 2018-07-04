import unicornhat as uc
import time

uc.brightness(.5)
uc.rotation(180)

x = 0
y = 0

try:
    while 1:

        for x in range(8):

            uc.set_pixel(x,y,128,0,0)
            uc.set_pixel(x-1,y,0,0,0)
            uc.show()
            time.sleep(.3)
            print(x)    

        for x in range(6, 0, -1):

            uc.set_pixel(x,y,128,0,0)
            uc.set_pixel(x+1,y,0,0,0)
            uc.show()
            time.sleep(.3)
            print(x)

        uc.set_pixel(1,y,0,0,0)

except KeyboardInterrupt:
    uc.off()
