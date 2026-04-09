from picozero import RGBLED, Button
from time import sleep
from machine import ADC
from math import log

led = RGBLED(6, 7, 8)
pot = ADC(27)
thermistor = ADC(28)
button = Button(13)
vIn = 3.3
resistorOne = 10000

# steinhart constants
A = 1.129e-3
B = 2.341e-4
C = 8.767e-8


def getTempC(thermistor, vIn, resistor, A, B, C):
    adcValue = thermistor.read_u16()
    vOut = (vIn / 65535) * adcValue
    Rt = (vOut * resistor) / (vIn - vOut)
    tempK = 1 / (A + (B * log(Rt)) + (C * pow(log(Rt), 3)))
    tempC = tempK - 273.15
    return tempC

def getTempF(tempC):
    tempF = ((tempC * (9 / 5)) + 32)
    return tempF



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

    sleep(.1)


while True:
    tempF = getTempF(getTempC(thermistor, vIn, resistorOne, A, B, C))
    potValue = pot.read_u16()
    setPoint = int((potValue * (40 / 65535) + 60))

    minTemp = setPoint - 2
    maxTemp = setPoint + 2

    if minTemp <= tempF <= maxTemp:
        led.color = (0, 255, 0)
    elif tempF > maxTemp:
        led.color = (255, 0, 0)
    elif tempF < minTemp:
        led.color = (0, 0, 255)

    feeling = setPoint - tempF
    if feeling == 0:
        status = "just right"
    elif feeling > 0:
        status = "too cold"
    elif feeling < 0:
        status = "too hot"

    print(f"setPoint: {setPoint} | tempF: {tempF} | diff: {setPoint - tempF} | Status: {status}")
    sleep(.1)
