'''
Write a function that converts a potentiometer's analog value to a temperature setpoint. The setpoint range is 10 °C to 40 °C. 

    Function name: updateSetpoint
    Parameters: the potentiometer's analog value
    Return: the temperature setpoint in °C
'''

potValue = 67

def updateSetpoint(potValue):
    return int((potValue * (30 / 65535) + 10))

integer = updateSetpoint(potValue)
print(integer)
