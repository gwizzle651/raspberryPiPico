from machine import ADC
from time import sleep
from picozero import Servo, RGBLED

led = RGBLED(6, 7, 8)
stickx = ADC(27)
sticky = ADC(26)
servo = Servo(15, min_pulse_width = .00055, max_pulse_width = .0024)
pot = ADC(28)

uflag = False
dflag = False
lflag = False
rflag = False

print("to unlock the system you must move the joystick in the correct positions")
while uflag == False:
    stickyValue = sticky.read_u16()
    if stickyValue > 63000:
        uflag = True
    sleep(.1)

while dflag == False:
    stickxValue = stickx.read_u16()
    if stickyValue > 63000:
        dflag = True
    sleep(.1)

while lflag == False:
    stickxValue = stickx.read_u16()
    if stickyValue > 63000:
        lflag = True
    sleep(.1)

while rflag == False:
    stickxValue = stickx.read_u16()
    if stickyValue > 63000:
        rflag = True
    sleep(.1)

sleep(1)

while True:
    potValue = pot.read_u16()
    print(potValue)

    servo.value = (potValue / 65535)

    if servo.value == 1:
        led.color = (255, 0, 0)
    elif servo.value == 0:
        led.color = (0, 255, 0)
    else:
        led.color = (0, 0, 0)

    sleep(.1)
