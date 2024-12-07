from tree import set_string
from color_conversion import rgb_to_hsv, hsv_to_rgb

color = (1, 0, 0)
r, g, b = color
h, s, v = rgb_to_hsv(r, g, b)

while True:
    r, g, b = hsv_to_rgb(h, s, v)
    set_string(1, int(255*r), int(255*g), int(255*b))
    h += 1 / 60
