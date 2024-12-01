from tree import set_string_brightness, setcolour, numLEDs, update_LED_string

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

set_string_brightness(1)

while True:
    for color in colors:
        r, g, b = color
        for i in range(numLEDs):
            setcolour(i, r, g, b)
            update_LED_string()
