from tree import set_string
from time import sleep

colors = [(128, 0, 0), (0, 128, 0), (0, 0, 128)]

while True:
    
    for color in colors:
        r, g, b = color
        set_string(10, r, g, b)
        sleep(1)
