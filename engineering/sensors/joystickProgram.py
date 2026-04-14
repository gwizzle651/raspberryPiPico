from machine import ADC # ADC means analog to digital converter
from time import sleep
from picozero import RGBLED, Button

led = RGBLED(10, 11, 12)
xJoystick = ADC(27)
yJoystick = ADC(26)
zButton = Button(22)

oldZButtonState = zButton.is_pressed
ledFlag = False

while True:
    xValue = xJoystick.read_u16()
    yValue = xJoystick.read_u16()
    newZButtonState = zButton.is_pressed
    print(f"X: {xValue}; Y: {yValue}; Z: {newZButtonState}")

    if oldZButtonState == True and newZButtonState == False:
        ledFlag = not ledFlag
        print(ledFlag)

    oldZButtonState = newZButtonState

    if ledFlag == True:
        redColor = int((255/65535) * xValue)
        greenColor = int((255/65535) * xValue)
        led.color = (redColor, greenColor, 255)
    else:
        led.color = (0, 0, 0)

    sleep(.1)

