from machine import Pin, SoftSPI

# Mapping of SPI for the LED string. miso is unused, but must be supplied.
# From initial experiments, 30K baudrate is just fast enough to make it appear
# all LEDs are updated simultaneously.
spi = SoftSPI(baudrate=30000, sck=Pin(28), mosi=Pin(12), miso=Pin(27))

numLEDs = 25
header_len = 4
frame_len = 4

# enough bytes to update all of the LEDs
# format is
#
# header: 0x0 0x0 0x0 0x0
# LEDn: 0b11100000 | brightness blue green red
# end: 0xff 0xff 0xff 0xff
data = bytearray(header_len + numLEDs*frame_len + header_len)

# initialise to set all 25 LEDs off/zero brightness
for i in range(header_len + numLEDs*frame_len, header_len + numLEDs*frame_len + header_len): data[i] = 0xff
for i in range(header_len, header_len + numLEDs*frame_len, frame_len): data[i] = 0b11100000

def refreshtree():
    spi.write(data)

# an order that traverses bottom to top on each leaf clockwise.
display_index1 = [0,  1,  2, 16, 17, 18, 15, 14, 13,  6,  5,  4, 12, 11, 10, 24, 23, 22, 19, 20, 21,  7,  8,  9, 3]

# an order that traverses clockwise around the bottom, and then upwards.
display_index  = [0, 16, 15,  6, 12, 24, 19,  7,  1, 17, 14,  5, 11, 23, 20,  8,  2, 18, 13,  4, 10, 22, 21,  9, 3]


def setpixeloff(offset):
    setpixel(offset, 0, 0, 0, 0)    


def setpixel(offset, brightness, r, g, b):
    global data
    ledFrame = header_len + offset*frame_len
    data[ledFrame] = 0b11100000 | brightness
    data[ledFrame+1] = b
    data[ledFrame+2] = g
    data[ledFrame+3] = r

def settree(brightness, r, g, b):
    for i in range(numLEDs):
        setpixel(i, brightness, r, g, b)
    refreshtree()
