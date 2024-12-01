from tree import setpixel, numLEDs, update_LED_string, spatial_ring, setbrightness, setpixeloff, settree, spatial_star
from time import sleep
from random import randint

while True:
    
    for i in range(numLEDs):
        setpixeloff(i)
    
    update_LED_string()
    
    for i in range(numLEDs - 1):
        setpixel(spatial_ring[i], randint(1, 8)*4-1, randint(0, 255), randint(0, 255), randint(0, 255))
        update_LED_string()
        sleep(0.1 * randint(1, 10))

    # flash the top LED    
    setpixel(spatial_star, 10, 255, 255, 0)
    update_LED_string()
    sleep(0.2)

    setbrightness(spatial_star, 0)
    update_LED_string()
    sleep(0.2)

    setpixel(spatial_star, 10, 255, 255, 0)
    update_LED_string()
    sleep(0.2)