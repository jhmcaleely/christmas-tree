from machine import Pin, ADC
from time import sleep
from tree import settree, setcolour, update_LED_string, set_string_brightness, spatial_ring


# Pico LiPo features
charging = Pin(24, Pin.IN)
vsys = ADC(Pin(29, Pin.IN))

full_battery = 4.2
empty_battery = 2.8

def batt_percentage(voltage):
    percentage = 100 * ((voltage - empty_battery) / (full_battery - empty_battery))
    return percentage

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

    
