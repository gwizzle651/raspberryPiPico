################################
###### import libraries ########
################################
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep


################################
### Specify pins and objects ###
################################

# OLED object
display_width = 128 # pixel x values = 0 to 127
display_height = 64 # pixel y values = 0 to 63
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000) # TX pin is Pin 0, RX pin is Pin 1
display = SSD1306_I2C(display_width, display_height, i2c)


################################
####### Other setup stuff ######
################################


################################
######## Infinite Loop #########
################################
while True:
    # Clear entire display
    display.fill(0) # clear entire display
    display.show() # make the changes take effect
    
    sleep(1)
    
    # Erase everything and write text
    display.fill(0) # clear entire display
    display.text("I love ice cream", 0, 0) # write text starting at x=0 and y=0
    display.show() # make the changes take effect
    
    sleep(1)
    
    # Draw an empty box without erasing anything
    display.rect(10, 10, 50, 30, 1) # draw empty rectangle starting at x=10, y=10, width=50, height=30, color=1
    display.show() # make the changes take effect
    
    sleep(1)
    
    # Draw a filled box without erasing anything
    display.fill_rect(5, 5, 60, 30, 1) # draw filled rectangle starting at x=5, y=5, width=60, height=30, color=1
    display.show() # make the changes take effect
    
    sleep(1)
    
    # Draw a single pixel without erasing anything
    display.pixel(64, 50, 1) # draw single pixel at x=64, y=50, color=1
    display.show()
    
    sleep(1)
    
    # Erase everything and draw a triangle
    display.fill(0)
    display.hline(10,10, 80, 1) # horizontal line 80px long from (10,10)
    display.vline(10,10, 35, 1) # vertical line 35px long from (10,10)
    display.line(10,45, 90,10, 1) # two-point line from (10,45) to (90,10)
    display.show()
    
    sleep(1)
