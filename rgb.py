from tree import settree
from time import sleep

colors = [(128, 0, 0), (0, 128, 0), (0, 0, 128)]

while True:
    
    for color in colors:
        r, g, b = color
        settree(10, r, g, b)
        sleep(1)
