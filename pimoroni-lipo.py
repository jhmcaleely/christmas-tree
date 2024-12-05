from machine import Pin, ADC
from time import sleep
from tree import settree, setcolour, numLEDs, update_LED_string, set_string_brightness, spatial_ring


# Pico LiPo features
button = Pin(23, Pin.IN)
charging = Pin(24, Pin.IN)
vsys = ADC(Pin(29, Pin.IN))

full_battery = 4.2
empty_battery = 2.8

set_string_brightness(1)

def batt_voltage(v):
    adc_level = v.read_u16()
    conversion_factor = 3 * 3.3 / 65535
    
    return adc_level * conversion_factor

def display_percentage(percentage):
    print(percentage)
    set_string_brightness(1)
    if percentage < 25:
        for n in range (8):
            setcolour(spatial_ring[n], 255, 0, 0)
        update_LED_string()
    elif percentage >= 25 and percentage < 50:
        for n in range (16):
            setcolour(spatial_ring[n], 0, 255, 0)
        update_LED_string()
    elif percentage >= 50 and percentage < 75:
        for n in range (24):
            setcolour(spatial_ring[n], 0, 255, 0)
        update_LED_string()
    else:
        settree(1, 0, 255, 0)

while True:
    sleep(0.5)
    
    voltage = batt_voltage(vsys)
    
    print(f'{voltage} {charging.value()}')
    if button.value() == 0:
        percentage = 100 * ((voltage - empty_battery) / (full_battery - empty_battery))
       # percentage = 24
        display_percentage(percentage)
    else:
        settree(0, 0, 0, 0)
    
