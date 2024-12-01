from tree import settree
from color_conversion import rgb_to_hsv, hsv_to_rgb

color = (0.5, 0, 0)
r, g, b = color
h, s, v = rgb_to_hsv(r, g, b)

while True:
    r, g, b = hsv_to_rgb(h, s, v)
    settree(10, int(255*r), int(255*g), int(255*b))
    h += 1 / 60
