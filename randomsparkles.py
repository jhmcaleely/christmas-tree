from tree import setcolour, numLEDs, update_LED_string, set_string_brightness
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

set_string_brightness(1)

while True:
    pixel = random.randint(0, numLEDs-1)
    r, g, b = random_color()
    setcolour(pixel, r, g, b)
    update_LED_string()