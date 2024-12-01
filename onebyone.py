from tree import setpixel, numLEDs, refreshtree

colors = [(128, 0, 0), (0, 128, 0), (0, 0, 128)]

while True:
    for color in colors:
        r, g, b = color
        for i in range(numLEDs):
            setpixel(i, 10, r, g, b)
            refreshtree()
