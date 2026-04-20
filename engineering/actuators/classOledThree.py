from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep

# OLED object
display_width = 128 # pixel x values = 0 to 127
display_height = 64 # pixel y values = 0 to 63
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000) # TX pin is Pin 0, RX pin is Pin 1
display = SSD1306_I2C(display_width, display_height, i2c)

# Joystick pins
x_joystick_pin = ADC(27)

while True:
    # Read joystic x-axis value (0 - 65535)
    x_joystick_value = x_joystick_pin.read_u16()

    # Clear display and write value
    display.fill(0) # clears display
    display.text("ADC Value:", 0, 10) # display text starting at x=0, y=10
    display.text(str(x_joystick_value), 0, 40) # convert value to string and display it starting at x=0
    display.show()

    sleep(0.1)

