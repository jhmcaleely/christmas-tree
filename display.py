from tree import set_pixel, numLEDs, update_LED_string, spatial_ring, set_brightness, set_pixel_off, set_string, spatial_star
from time import sleep
from random import randint

while True:
    
    for i in range(numLEDs):
        set_pixel_off(i)
    
    update_LED_string()
    
    for i in range(numLEDs - 1):
        set_pixel(spatial_ring[i], randint(1, 8)*4-1, randint(0, 255), randint(0, 255), randint(0, 255))
        update_LED_string()
        sleep(0.1 * randint(1, 10))

    # flash the top LED    
    set_pixel(spatial_star, 10, 255, 255, 0)
    update_LED_string()
    sleep(0.2)

    set_brightness(spatial_star, 0)
    update_LED_string()
    sleep(0.2)

    set_pixel(spatial_star, 10, 255, 255, 0)
    update_LED_string()
    sleep(0.2)
    