#moving redsnake

import unicornhat as uc
import time

uc.brightness(.4)
uc.rotation(180)

try:
    while 1:

        for x in range (0, 18,):

            points = [(0,0), (1,0), (2,1), (3,1), (4,2), (5,3), (5,4), (6,5), (5,6), (4,7), (3,7), (2,7), (1,6), (0,5), (0,4), (1,3), (1,2), (0,1)]
            uc.set_all(0,110,0)
            
            for y in range (0,9):
                colors = [(255,0,0), (230,0,0), (205,0,0), (180,0,0), (155,0,0), (130,0,0), (115,0,0), (80,0,0), (0,128,0)]
                uc.set_pixel(points[x-y][0],points[x-y][1],colors[y][0],colors[y][1],colors[y][2])
                
            uc.show()
            time.sleep(.4)
    
except KeyboardInterrupt:
    uc.off()

