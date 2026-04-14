from picozero import Button, Speaker
from time import sleep

button = Button(2)
speaker = Speaker(16)

notes = ["c4", "d4", "e4", "f4", "g2"]

rhythm = [
    ("e5", .35, .15),
    ("d5", .35, .15),
    ("c5", .35, .15),
    ("d5", .35, .15),

    ("e5", .5, .2),
    ("e5", .35, .15),
    ("e5", .5, .2),

    ("d5", .5, .2),
    ("d5", .35, .15),
    ("d5", .5, .2),

    ("e5", .35, .15),
    ("g5", .35, .15),
    ("g5", .5, .2),

    ("e5", .35, .15),
    ("d5", .35, .15),
    ("c5", .35, .15),
    ("d5", .35, .15),

    ("e5", .5, .2),
    ("e5", .35, .15),
    ("e5", .5, .2),

    ("d5", .5, .2),
    ("d5", .35, .15),
    ("e5", .35, .15),
    ("d5", .75, .3),
]

'''
def playNotes(notes):
    if not duration:
        duration = .1
    volume = .25

    for note in notes:
        speaker.play(note, duration, volume)
        sleep(.05)
    speaker.off()
'''

def playRhythm(rhythm):
    for note in notes:
        speaker.play(rhythm)
    speaker.off()

readyState = button.value
print("press the button to continue...")
sleep(.5)

while not readyState:
    if button.value == True:
        readyState = True
        print("starting main loop...")
        sleep(2)

    sleep(.1)

while True:
    playRhythm(rhythm)

    if button.is_pressed() == True:
        speaker.on()
    else:
        speaker.off()

