# christmas-tree

Raspberry Pi Pico Micropython and Yarg code for [The Pi Hut 3D Xmas Tree for Rasberry Pi][tree].

The original board is designed as a Hat for 40-pin Raspberry Pi boards. On these boards, using the SPI to transmit the signal the LEDs need is convenient. This repo is for a Raspberry Pi Pico to drive this via a suitable adaptor.

There's no specific hardware diagram from The Pi Hut, but the [conversation here][forum thread] helps to clarify that the design appears to be for 2-wire SPI driving a string of LEDs.

Which LEDs are not clarified, but it seems reasonable to speculate they are similar to [these at adafruit][dotstar]. The latest code in this repo successfully asssumes they are a string of APA102 LEDs.

I've wired the board to the Pico assuming I will use these as a [converter from 40-pin to pico][40-pin-pico] in hardware. As such, the LED clock appears on GPIO 28 (Pico pin 34) and the data pin appears on GPIO 9 (Pico pin 12).

I use the PIO code from: https://github.com/raspberrypi/pico-examples/tree/master/pio/apa102

The Micropython code currently uses Software SPI to drive the LEDs in the same manner as the sample code from The Pi Hut.

[tree]: https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi
[forum thread]: https://forums.raspberrypi.com/viewtopic.php?t=260938
[dotstar]: https://www.adafruit.com/product/2343
[40-pin-pico]: https://thepihut.com/products/pico-to-pi-hat
