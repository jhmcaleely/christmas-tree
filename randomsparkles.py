from tree import setpixel, numLEDs, refreshtree
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

while True:
    pixel = random.randint(0, numLEDs-1)
    r, g, b = random_color()
    setpixel(pixel, 1, r, g, b)
    refreshtree()