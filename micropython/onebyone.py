from tree import set_string_brightness, set_color, numLEDs, update_LED_string, spatial_leaf

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

set_string_brightness(1)

while True:
    for color in colors:
        r, g, b = color
        for i in range(numLEDs):
            set_color(spatial_leaf[i], r, g, b)
            update_LED_string()
