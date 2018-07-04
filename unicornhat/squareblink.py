#blinks in red around perimiter
import unicornhat as uc
import time

uc.brightness(.5)
uc.rotation(180)

x = 0
y = 0

try:
    while 1:

        for x in range (-1, 8):

            uc.set_pixel(x,y,128,0,0)
            uc.set_pixel(x-1,y,0,0,0)
            uc.show()
            time.sleep(.3)

        uc.set_pixel(7,0,0,0,0)
        uc.show

        for y in range (0, 8)

            uc.set_pixel(7,y,128,0,0,0)
            uc.set_pixel(7,y-1,0,0,0)
            uc.show()
            time.sleep(.3)

        uc.set_pixel(7,7,0,0,0)
        uc.show()

        for x in range (7, -1, -1)

            uc.set_pixel(x,7,128,0,0)
            uc.set_pixel(x+1,7,0,0,0)
            uc.show()
            time.sleep(.3)

        uc.set_pixel(0,7,0,0,0)
        uc.show()

        for y in range (7, 0, -1)

            uc.set_pixel(0,y,128,0,0)
            uc.set_pixel(0,y+1,0,0,0)
            uc.show()
            time.sleep(.3)

        uc.set_pixel(0,1,0,0,0)

except KeyboardInterrupt:
    uc.off()
        
