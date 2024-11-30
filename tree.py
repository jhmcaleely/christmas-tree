from machine import Pin, SoftSPI
from time import sleep

piLED = Pin(25, Pin.OUT, value = 1)

#spi = SPI(0, baudrate=400000, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
spi= SoftSPI(baudrate=30000, sck=Pin(28), mosi=Pin(12), miso=Pin(27))
print(spi)

data = bytearray(4+25*4+4)
data[0] = 0
data[1] = 0
data[2] = 0
data[3] = 0

data[104] = 0xf
data[105] = 0xf
data[106] = 0xf
data[107] = 0xf


def setpixeloff(offset):
    setpixel(offset, 0, 0, 0, 0)    


def setpixel(offset, brightness, r, g, b):
    global data
    ledFrame = 4 + offset*4
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

    for i in range(25):
        setpixeloff(i)
    
    sleep(2.15)

    spi.write(data)
    
    sleep(5.15)

    