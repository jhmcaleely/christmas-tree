from machine import Pin, SoftSPI

# Mapping of SPI for the LED string. miso is unused, but must be supplied.
# From initial experiments, 30K baudrate is just fast enough to make it appear
# all LEDs are updated simultaneously.
spi = SoftSPI(baudrate=30000, sck=Pin(28), mosi=Pin(12), miso=Pin(27))

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

# an order that traverses bottom to top on each leaf clockwise.
spatial_leaf = [0,  1,  2, 16, 17, 18, 15, 14, 13,  6,  5,  4, 12, 11, 10, 24, 23, 22, 19, 20, 21,  7,  8,  9, spatial_star]

# an order that traverses clockwise around the bottom, and then upwards over three rings.
spatial_ring = [0, 16, 15,  6, 12, 24, 19,  7,  1, 17, 14,  5, 11, 23, 20,  8,  2, 18, 13,  4, 10, 22, 21,  9, spatial_star]

def LEDn_frame_offset(n):
    return LED0_frame + n * frame_len

def setpixeloff(offset):
    setbrightness(offset, 0)    

def setbrightness(n, brightness):
    global message
    message[LEDn_frame_offset(n)]   = 0b11100000 | brightness
    
def setcolour(n, r, g, b):
    global message
    LEDn_frame = LEDn_frame_offset(n)
    message[LEDn_frame+1] = b
    message[LEDn_frame+2] = g
    message[LEDn_frame+3] = r    
    
def setpixel(n, brightness, r, g, b):
    global message
    LEDn_frame = LEDn_frame_offset(n)
    message[LEDn_frame]   = 0b11100000 | brightness
    message[LEDn_frame+1] = b
    message[LEDn_frame+2] = g
    message[LEDn_frame+3] = r

def set_string_brightness(brightness):
    for i in range(numLEDs):
        setbrightness(i, brightness)
    update_LED_string()

def settree(brightness, r, g, b):
    for i in range(numLEDs):
        setpixel(i, brightness, r, g, b)
    update_LED_string()
