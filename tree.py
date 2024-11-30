from machine import Pin, SoftSPI
from time import sleep

piLED = Pin(25, Pin.OUT, value = 1)

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



def setpixeloff(offset):
    setpixel(offset, 0, 0, 0, 0)    


def setpixel(offset, brightness, r, g, b):
    global data
    ledFrame = header_len + offset*frame_len
    data[ledFrame] = 0b11100000 | brightness
    data[ledFrame+1] = b
    data[ledFrame+2] = g
    data[ledFrame+3] = r
    
def setpattern():
    setpixel(0, 15, 255, 0, 0)
    setpixel(1, 15, 0, 255, 0)
    setpixel(2, 15, 0, 0, 255)
    setpixel(3, 2, 255, 255, 255)
    setpixel(4, 2, 255, 255, 255)
    setpixel(5, 2, 255, 255, 255)
    setpixel(6, 2, 255, 0, 255)
    setpixel(7, 2, 255, 255, 255)
    setpixel(8, 2, 255, 255, 255)
    setpixel(9, 2, 255, 255, 255)
    setpixel(10, 2, 255, 255, 255)
    setpixel(11, 2, 255, 255, 255)
    setpixel(12, 2, 255, 255, 255)
    setpixel(13, 2, 255, 255, 255)
    setpixel(14, 2, 255, 255, 255)
    setpixel(15, 2, 255, 255, 255)
    setpixel(16, 2, 255, 0, 255)
    setpixel(17, 2, 255, 255, 255)
    setpixel(18, 2, 255, 255, 255)
    setpixel(19, 2, 255, 255, 255)
    setpixel(20, 2, 255, 255, 255)
    setpixel(20, 2, 0, 255, 0)
    setpixel(21, 2, 255, 255, 255)
    setpixel(22, 2, 255, 255, 255)
    setpixel(23, 2, 255, 255, 255)
    setpixel(24, 2, 255, 255, 255)

while True:
    setpattern()
    spi.write(data)

    for i in range(numLEDs):
        setpixeloff(i)
    
    sleep(2.15)

    spi.write(data)
    
    sleep(5.15)

    