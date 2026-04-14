readyState = button.value
print("press the button to continue...")
sleep(2)

while not readyState:
    if button.value == True:
        readyState = True
        led.color = (255, 0, 0)
        print("starting main loop...")
        sleep(2)
        led.toggle()

    sleep(.1)
