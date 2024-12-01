from tree import setpixel, numLEDs, refreshtree, display_index, setpixeloff, settree
from time import sleep
from random import randint

while True:
    
    for i in range(numLEDs):
        setpixeloff(i)
    
    for i in range(numLEDs - 1):
        setpixel(display_index[i], randint(1, 4), randint(0, 255), randint(0, 255), randint(0, 255))
        refreshtree()
        sleep(0.1 * randint(1, 10))

    # flash the top LED
    setpixel(display_index[numLEDs-1], 10, 255, 255, 255)
    refreshtree()
    sleep(0.2)

    setpixeloff(display_index[numLEDs-1])
    refreshtree()
    sleep(0.2)

    setpixel(display_index[numLEDs-1], 10, 255, 255, 255)
    refreshtree()
    sleep(0.2)