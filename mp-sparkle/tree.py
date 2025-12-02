from machine import Pin, SoftSPI

# Raspberry Pi Pico SPI based driver for The Pi Hut 3D RGB Xmas Tree for Rasbperry Pi.
#
# The 3D RGB Xmas tree is documented in it's sample code, and is designed to be connected
# to a 40-pin Raspberry Pi HAT connector. It appears to require four connections
# - power, ground, clock and data. It seems likely the 25 LEDs are something similar to the
# Adafruit DotStar LEDs, and appear to be driven via a 2-wire SPI protocol.
# The LED's seem to be unfussy about power voltage (so 3.3v or 5v seems fine) and clock timing.
# The 40-pin connector has the clock wire on GPIO25 and the data wire on GPIO12
# (a nod to 12/25 as the date of christmas for the designer!)
#
# Mapping of SPI for the LED string. miso is unused, but must be supplied to SoftSPI.
# From initial experiments, 30K baudrate is just fast enough to make it appear
# all LEDs are updated simultaneously.
# Note that miso needs to be parked on an innocent (unconnected?) gpio. 16 seems fine.
# For the HardStuff Pico HAT adaptor, RP2040 GPIO 9 (exposed on Pico pin 12) maps to HAT GPIO 12,
# and Pico GPIO 28 maps to HAT GPIO 25
spi = SoftSPI(baudrate=30000, sck=Pin(28), mosi=Pin(9), miso=Pin(16))

numLEDs = 25

# enough bytes to update all of the LEDs
# format is
#
# header: 0x0 0x0 0x0 0x0
# LEDn: 0b11100000 | brightness blue green red
# end: 0xff 0xff 0xff 0xff

frame_len = 4
start_frame = 0
LED0_frame = start_frame + frame_len
end_frame = frame_len + numLEDs * frame_len

message = bytearray(frame_len + numLEDs * frame_len + frame_len)

for i in range(end_frame, end_frame + frame_len): message[i] = 0xff

# initialise to set all 25 LEDs off/zero brightness
for i in range(LED0_frame, end_frame, frame_len): message[i] = 0b11100000

def update_LED_string():
    spi.write(message)
    

# index of the LED in the tree's star/top position.
spatial_star = 3

# an order that traverses bottom to top on each leaf clockwise, with the star last.
spatial_leaf = [0,  1,  2, 16, 17, 18, 15, 14, 13,  6,  5,  4, 12, 11, 10, 24, 23, 22, 19, 20, 21,  7,  8,  9, spatial_star]

# an order that traverses clockwise around the bottom, and then upwards over three rings. Finally the star is addressed.
spatial_ring = [0, 16, 15,  6, 12, 24, 19,  7,  1, 17, 14,  5, 11, 23, 20,  8,  2, 18, 13,  4, 10, 22, 21,  9, spatial_star]

def LEDn_frame_offset(n):
    return LED0_frame + n * frame_len

def set_pixel_off(n):
    set_brightness(n, 0)    

def set_brightness(n, brightness):
    global message
    message[LEDn_frame_offset(n)] = 0b11100000 | brightness
    
def set_color(n, r, g, b):
    global message
    LEDn_frame = LEDn_frame_offset(n)
    message[LEDn_frame+1] = b
    message[LEDn_frame+2] = g
    message[LEDn_frame+3] = r    
    
def set_pixel(n, brightness, r, g, b):
    global message
    LEDn_frame = LEDn_frame_offset(n)
    message[LEDn_frame]   = 0b11100000 | brightness
    message[LEDn_frame+1] = b
    message[LEDn_frame+2] = g
    message[LEDn_frame+3] = r

def set_string_brightness(brightness):
    for i in range(numLEDs):
        set_brightness(i, brightness)
    update_LED_string()

def set_string_color(r, g, b):
    for i in range(numLEDs):
        set_color(n, r, g, b)
    update_LED_string()

def set_string(brightness, r, g, b):
    for i in range(numLEDs):
        set_pixel(i, brightness, r, g, b)
    update_LED_string()

def display_percentage(percentage):
    if percentage < 25:
        for n in range (8):
            set_pixel(spatial_ring[n], 1, 255, 0, 0)
        for n in range (8, numLEDs):
            set_pixel_off(spatial_ring[n])
        update_LED_string()
    elif percentage >= 25 and percentage < 50:
        for n in range (16):
            set_pixel(spatial_ring[n], 1, 0, 255, 0)
        for n in range (16, numLEDs):
            set_pixel_off(spatial_ring[n])
        update_LED_string()
    elif percentage >= 50 and percentage < 75:
        for n in range (24):
            set_pixel(spatial_ring[n], 1, 0, 255, 0)
        for n in range (24, numLEDs):
            set_pixel_off(spatial_ring[n])
        update_LED_string()
    else:
        set_string(1, 0, 255, 0)