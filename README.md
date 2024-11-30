# christmas-tree

Christmas Tree novelty for Raspberry Pi Pico

Raspberry Pi Pico/Micropython code for [The Pi Hut 3D Xmas Tree for Rasberry Pi][tree].

The original board is designed as a Hat for the 40-pin Raspberry Pi boards.

Sample code is supplied here: https://github.com/ThePiHut/rgbxmastree

There's no specific hardware diagram, but the [conversation here][forum thread] helps to clarify that the design appears to be for 2-wire SPI driving a string of LEDs.

Which LEDs are not clarified, but it seems reasonable to speculate they are similar to [these at adafruit][dotstar].

The datasheet for those does line up nicely with the sample code, and if we assume it is correct, then it points to a bug in the smaple code - the end frame needs to be all 1's and 4 bytes long (not 5 bytes of zero as the sample seems to use).

I've wired the board to the Pico assuming I will use these as a [converter from 40-pin to pico][40-pin-pico] in hardware. As such, the SPI clock appears on GPIO 27 and the TX (mosi) appears on GPIO12 for the pico. This doesn't match the Pico's hardware SPI, so I use the software SPI.


[tree]: https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi
[forum thread]: https://forums.raspberrypi.com/viewtopic.php?t=260938
[dotstar]: https://www.adafruit.com/product/2343
[40-pin-pico]: https://thepihut.com/products/pico-to-pi-hat