import rp2
from time import sleep
from machine import Pin

led = Pin("LED", Pin.OUT)

# both of the following turn off the LED
led.value(False)
# led.off()

def blinkOnce():
    led.value(True)
    sleep(.5)
    led.value(False)
    sleep(.5)

while True:
    # print the value of the button (one or zero, with zero being not pressed)
    # print(rp2.bootsel_button())
    if (rp2.bootsel_button()):
        blinkOnce()

    sleep(.05)

