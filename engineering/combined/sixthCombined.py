from time import sleep, ticks_ms, ticks_diff
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from math import log
from picozero import Button

def requireAction(action, xJoystick, yJoystick):
    if action == "left":
        xMove = -64535
        signifier = "x"
    elif action == "right":
        xMove = 64535
        signifier = "x"
    elif action == "up":
        yMove = 64535
        signifier = "y"
    elif action == "down":
        yMove = -64535
        signifier = "y"

    done = False
    while not done:
        xValue = xJoystick.read_u16()
        yValue = yJoystick.read_u16()

        if action == "left":
            if xMove >= xValue:
                done = True
        elif action == "right":
            if xMove <= xValue:
                done = True
        elif action == "up":
            if xMove >= yValue:
                done = True
        elif action == "down":
            if xMove <= yValue:
                done = True


xJoystick = ADC(27)
yJoystick = ADC(26)
button = Button(22)

display_width = 128
display_height = 64
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
display = SSD1306_I2C(display_width, display_height, i2c)

relaySignal = Pin(21, Pin.OUT)
relaySignal.value(0)

display.fill(0)
display.text("left-right-left-right", 0, 0)
display.show()
sleep(1)

lastTime = ticks_ms()

code = ["left", "right", "left", "right"]
for i in range(4):
    requireAction(code[i])

now = ticks_ms()
deltaTime = ticks_diff(now, lastTime) / 1000

if deltaTime > 3:
    quit()

while True:
    buttonState = button.is_pressed

