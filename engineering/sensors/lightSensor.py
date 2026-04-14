from picozero import RGBLED
from machine import Pin, ADC
from time import sleep

redPin = 2
greenPin = 3
bluePin = 4
led = RGBLED(redPin, greenPin, bluePin)
# led.color = (0, 0, 0)
# led.toggle()

ldrAO = ADC(26)
ldrDO = Pin(28, Pin.IN)


while True:
    lightValue = ldrAO.read_u16()
    lightState = ldrDO.value()
    print(lightValue, lightState)

    ledColor = int((255/65535) * lightValue)
    ledColorInverted = int((-255/65535) * lightValue)
 
    led.color = (ledColorInverted, 0, 0)

    sleep(.25)

