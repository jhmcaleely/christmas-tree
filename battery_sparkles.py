from tree import setcolour, numLEDs, update_LED_string, set_string_brightness
import random
from time import sleep
from machine import Pin
from pimoroni_lipo import batt_voltage, batt_percentage, display_percentage, vsys

# bit of a hack, so that the USB serial appears to initialise correctly
sleep(1)

button = Pin(23, Pin.IN)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

set_string_brightness(1)

while True:
        
    if button.value() == 0:
        voltage = batt_voltage(vsys)
        percentage = batt_percentage(voltage)
        display_percentage(percentage)
    else:
        pixel = random.randint(0, numLEDs-1)
        r, g, b = random_color()
        setcolour(pixel, r, g, b)
        update_LED_string()
