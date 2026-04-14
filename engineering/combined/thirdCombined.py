from machine import ADC
from time import sleep
from picozero import RGBLED, Button

led = RGBLED(6, 7, 8)
pot = ADC(28)
xJoystick = ADC(27)
yJoystick = ADC(26)
button = Button(22)

readyState = button.value
print("press the button to continue...")
sleep(2)

while not readyState:
    if button.value == True:
        readyState = True
        led.color = (255, 0, 0)
        print("starting main loop...")
        sleep(2)
        led.toggle()

    sleep(.1)

while True:
    xValue = xJoystick.read_u16()
    yValue = xJoystick.read_u16()
    buttonValue = button.value
    potValue = pot.read_u16()
    colorStrength = int((255 / 65535) * potValue)

    if xValue < 25000:
        led.color = (colorStrength, 0, colorStrength)
    elif xValue > 35000:
        led.color = (0, 0, colorStrength)
    elif yValue < 25000:
        led.color = (0, colorStrength, 0)
    elif yValue > 35000
        led.color = (colorStrength, 0, 0)
    else:
        led.color = (0, 0, 0)

    sleep(.1)

