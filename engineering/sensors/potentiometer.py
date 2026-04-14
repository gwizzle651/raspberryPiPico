from picozero import RGBLED
from time import sleep
from machine import ADC
from math import log

led = RGBLED(6, 7, 8)
pot = ADC(26)
thermistor = ADC(27)
vIn = 3.3
resistorOne = 10000

# steinhart constants
A = 1.129e-3
B = 2.341e-4
C = 8.767e-8


def calculateTemperatureCelsius(thermistor, vIn, resistor, A, B, C):
    adcValue = thermistor.read_u16()
    vOut = (vIn / 65535) * adcValue
    Rt = (vOut * resistor) / (vIn - vOut)
    tempK = 1 / (A + (B * log(Rt)) + (C * pow(log(Rt), 3)))
    tempC = tempK - 273.15
    return tempC


while True:
    potValue = pot.read_u16()
    setpoint = ((15/65535) * potValue) + 15
    tempC = calculateTemperatureCelsius(thermistor, vIn, resistorOne, A, B, C)

    print(f"Potentiometer: {potValue} | Temperature: {tempC}")

    if setpoint > tempC:
        led.color = (255, 0, 0)
    elif setpoint <= tempC:
        led.color = (0, 0, 255)

    sleep(.1)

