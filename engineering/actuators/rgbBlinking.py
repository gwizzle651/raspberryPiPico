from picozero import RGBLED
from time import sleep, ticks_ms, ticks_diff

redPin = 18
greenPin = 19
bluePin = 20

led = RGBLED(redPin, greenPin, bluePin)
lastTime = ticks_ms()
led.color = (150, 0, 150)

while True:
    now = ticks_ms()
    deltaTime = ticks_diff(now, lastTime) / 1000 # divide by 1000 in order to turn miliseconds into seconds.

    if deltaTime > 1:
        led.toggle()
        lastTime = ticks_ms()

    sleep(.5)

