from picozero import RGBLED
from time import sleep
from math import log
from machine import ADC

redPin = 6
greenPin = 7
bluePin = 8
led = RGBLED(redPin, greenPin, bluePin)
led.color = (255, 0, 0)

thermistor = ADC(26)
vIn = 3.3
resistorOne = 10000

# steinhart constants
A = 1.129e-3
B = 2.341e-4
C = 8.767e-8


def calculateTemperature(thermistor, vIn, resistor, A, B, C):
    adcValue = thermistor.read_u16()
    vOut = (vIn / 65535) * adcValue
    Rt = (vOut * resistor) / (vIn - vOut)
    tempK = 1 / (A + (B * log(Rt)) + (C * pow(log(Rt), 3)))
    tempC = tempK - 273.15
    return tempC


sleep(1)

while True:
   temperature = calculateTemperature(thermistor, vIn, resistorOne, A, B, C)
   print(temperature)
   sleep(.5)

