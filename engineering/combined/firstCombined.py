from picozero import RGBLED
from time import sleep
from math import log
from machine import Pin, ADC

# rgb led
redPin = 6
greenPin = 7
bluePin = 8
led = RGBLED(redPin, greenPin, bluePin)

# temperature sensor
thermistor = ADC(28)
vIn = 3.3
resistorOne = 10000
# steinhart constants for temperature sensor
A = 1.129e-3
B = 2.341e-4
C = 8.767e-8

# light sensor
ldrDO = Pin(20, Pin.IN)
ldrAO = ADC(26)


def calculateTemperature(thermistor, vIn, resistor, A, B, C):
    adcValue = thermistor.read_u16()
    vOut = (vIn / 65535) * adcValue
    Rt = (vOut * resistor) / (vIn - vOut)
    tempK = 1 / (A + (B * log(Rt)) + (C * pow(log(Rt), 3)))
    tempC = tempK - 273.15
    return tempC

def getLightValue(ldrDO, ldrAO):
    lightState = ldrDO.value()
    lightValue = ldrAO.read_u16()
    return (lightState, lightValue)


sleep(1)
while True:
    temperature = calculateTemperature(thermistor, vIn, resistorOne, A, B, C)
    thresh = 25

    lightData = getLightValue(ldrDO, ldrAO)
    lightState = lightData[0]
    lightValue = lightData[1]
    print(f"{lightState} | {lightValue}")


    ledColorStrength = int((-255/65535) * lightValue)

    if thresh >= temperature:
        led.color = (0, 0, ledColorStrength)

    elif thresh < temperature:
        led.color = (ledColorStrength, 0, 0)

    sleep(.25)

