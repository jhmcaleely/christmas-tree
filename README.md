# christmas-tree

Raspberry Pi Pico Micropython and Yarg code for [The Pi Hut 3D Xmas Tree for Rasberry Pi][tree].

The original board is designed as a Hat for 40-pin Raspberry Pi boards. On these boards, using the SPI to transmit the signal the LEDs need is convenient. 

This repo is for a Raspberry Pi Pico to drive this via a suitable adaptor. Implementations in three languages are present: C, [MicroPython][micropython] and [Yarg][yarg-lang].

## c-sparkle

This is a lightly edited copy of the Pico SDK example '[pio/apa102][sdk-example]', which will directly support this christmas tree. It uses PIO to generate the required signal for the apa102 LEDs.

## micropython

This example evolved from the sample code for the Raspberry Pi, and uses SPI to generate the apa102 signal. Since the tree's pins do not correspond to the SPI pins on the pico, a software SPI driver is used.

## yarg-sparkle

Yarg Sparkle drives the tree using PIO that is hosted in the Yarg sources, so is implemented entirely in a dynamic language with no C drivers required.

## 3D Xmas Tree Details

There's no specific hardware diagram from The Pi Hut, but the [conversation here][forum thread] helps to clarify that the design appears to be for 2-wire SPI driving a string of LEDs.

Which LEDs are not clarified, but it seems reasonable to speculate they are similar to [these at adafruit][dotstar]. The latest code in this repo successfully asssumes they are a string of APA102 LEDs.

## Pico Converter

This repo uses these adaptors as a [converter from 40-pin to pico][40-pin-pico]. As such, the tree's LED clock appears on GPIO 28 (Pico pin 34) and the data pin appears on GPIO 9 (Pico pin 12).

## PIO for apa102

The PIO code is from the [Pico SDK examples][sdk-exampple], and is the same PIO program in the C and Yarg implementations.

[tree]: https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi
[forum thread]: https://forums.raspberrypi.com/viewtopic.php?t=260938
[dotstar]: https://www.adafruit.com/product/2343
[40-pin-pico]: https://thepihut.com/products/pico-to-pi-hat
[micropython]: https://micropython.org/
[yarg-lang]: https://yarg-lang.dev/
[sdk-example]: https://github.com/raspberrypi/pico-examples/tree/master/pio/apa102
