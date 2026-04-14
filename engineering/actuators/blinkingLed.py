from machine import Pin
from time import sleep, ticks_ms, ticks_diff

led = Pin("LED", Pin.OUT)
lastTime = ticks_ms()
ledStatus = False
led.value(ledStatus)

def main(ledStatus, lastTime):
    while True:
        now = ticks_ms() 
        deltaT = ticks_diff(now, lastTime) / 1000

        if (deltaT > 1):
            ledStatus = not ledStatus
            led.value(ledStatus)
            lastTime = ticks_ms()

        sleep(.05)

main(ledStatus, lastTime)
