from machine import Pin, ADC
from tree import set_string, numLEDs, set_pixel_off, set_pixel, update_LED_string, spatial_ring


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
