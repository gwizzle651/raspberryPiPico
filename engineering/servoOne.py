from machine import ADC
from time import sleep
from picozero import Servo

stickx = ADC(27)
sticky = ADC(26)
servo = Servo(2, min_pulse_width = .00055, max_pulse_width = .0024)

uflag = False
dflag = False

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

sleep(1)

while True:
    '''
    # rotate servo back and forth
    servo.value = 0
    sleep(.5)
    servo.value = 1
    sleep(.5)
    '''
    stickxValue = stickx.read_u16()
    print(stickxValue)

    servo.value = (stickxValue / 65535)
    sleep(.1)
