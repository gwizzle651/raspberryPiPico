from picozero import RGBLED, Button
from time import sleep

led = RGBLED(10, 11, 12)
button = Button(22)
led.color = (255, 0, 0)
counter = 0

# check for button press
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

# teacher method
'''
oldButtonState = button.is_pressed

while readyState = False:
    newButtonState = button.is_pressed
    if oldButtonState == True and newButtonState == False:
        readyState = True

    oldButtonState = newButtonState
    print(readyState)
    sleep(.1)
'''

while True:
    led.color = (counter, 0, 0)
    counter += 1

    if counter > 255:
        counter = 0

    print(counter)
    sleep(.1)
