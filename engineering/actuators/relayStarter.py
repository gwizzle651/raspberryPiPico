from time import sleep
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C

# OLED object
display_width = 128 # pixel x values = 0 to 127
display_height = 64 # pixel y values = 0 to 63
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000) # TX pin is Pin 0, RX pin is Pin 1
display = SSD1306_I2C(display_width, display_height, i2c)

relaySignal = Pin(2, Pin.OUT)

while True:
    relaySignal.value(0)
    display.fill(0) # clears display
    display.text("blue", 0, 0) # write text starting at x=0 and y=0
    display.show() # make the changes take effect
    sleep(1)

    relaySignal.value(1)
    display.fill(0) # clears display
    display.text("red", 0, 0) # write text starting at x=0 and y=0
    display.show() # make the changes take effect
    sleep(1)

