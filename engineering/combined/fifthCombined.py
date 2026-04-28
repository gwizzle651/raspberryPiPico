from time import sleep, ticks_ms, ticks_diff
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from math import log
from picozero import Button

xJoystick = ADC(27)
yJoystick = ADC(26)
button = Button(22)

thermistor = ADC(26)
vIn = 3.3
resistorOne = 10000

# steinhart constants
A = 1.129e-3
B = 2.341e-4
C = 8.767e-8


def calculateTemperatureC(thermistor, vIn, resistor, A, B, C):
    adcValue = thermistor.read_u16()
    vOut = (vIn / 65535) * adcValue
    Rt = (vOut * resistor) / (vIn - vOut)
    tempK = 1 / (A + (B * log(Rt)) + (C * pow(log(Rt), 3)))
    tempC = tempK - 273.15
    return tempC

def calculateTemperatureF(tempC):



# oled object
display_width = 128 # pixel x values = 0 to 127
display_height = 64 # pixel y values = 0 to 63
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000) # TX pin is Pin 0, RX pin is Pin 1
display = SSD1306_I2C(display_width, display_height, i2c)

relaySignal = Pin(9, Pin.OUT)

lastTime = ticks_ms
deltaTime = ticks_diff(now, lastTime) / 1000
firstFlag = False
clicks = 0



while not firstFlag:
    relaySignal.value(0)
    display.fill(0) # clears display
    display.text("click the button three times in quick successsion", 0, 0) # write text starting at x=0 and y=0
    display.show() # make the changes take effect
    sleep(1)

# do nested while loops




while True:
    xValue = xJoystick.read_u16()
    yValue = xJoystick.read_u16()
    newZButtonState = zButton.is_pressed
 
   temperature = calculateTemperatureF(thermistor, vIn, resistorOne, A, B, C)

# oldZButtonState = zButton.is_pressed

