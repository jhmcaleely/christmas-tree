from machine import Pin, ADC

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

