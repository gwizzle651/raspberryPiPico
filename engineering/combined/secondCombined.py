from picozero import RGBLED, Button
from machine import Pin, ADC
from time import sleep

led = RGBLED(6, 7, 8)
pot = ADC(27)

ldrAO = ADC(28)
ldrDO = Pin(21, Pin.IN)

button = Button(14)
led.color = (255, 0, 0)

readyState = button.value
print("press the button to continue...")
sleep(2)

while not readyState:
    if button.value == True:
        readyState = True
        led.color = (0, 255, 0)
        print("starting main loop...")
        sleep(2)
        led.toggle()

    led.toggle()
    sleep(.5)

while True:
    lightValue = ldrAO.read_u16()
    potValue = pot.read_u16()
    print(f"Light Value: {lightValue} | Pot Value: {potValue}\n")

    minimum = potValue - 3000
    maximum = potValue + 3000

    if minimum <= lightValue <= maximum:
        led.color = (0, 0, 255)
    elif lightValue > maximum:
        led.color = (255, 0, 0)
    elif lightValue < minimum:
        led.color = (0, 255, 0)

    sleep(.1)

