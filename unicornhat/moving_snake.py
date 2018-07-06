#moving redsnake

import unicornhat as uc
import time

uc.brightness(.4)
uc.rotation(180)

try:
    while 1:

        for x in range (0, 18,):

            points = [(0,0), (1,0), (2,1), (3,1), (4,2), (5,3), (5,4), (6,5), (5,6), (4,7), (3,7), (2,7), (1,6), (0,5), (0,4), (1,3), (1,2), (0,1)]

            uc.set_pixel(points[x][0],points[x][1],128,0,0)
            uc.set_pixel(points[x-4][0],points[x-4][1],0,0,0)
            uc.show()
            time.sleep(.3)
    
except KeyboardInterrupt:
    uc.off()

