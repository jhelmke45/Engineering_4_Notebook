import board
import digitalio
import time

led1 = digitalio.DigitalInOut(board.GP1)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP3)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

var = 10

while button.value == False:
    print('ready for liftoff')

for x in range (10):
    print(10-x)
    var = x
    led1.value = True
    time.sleep(.5)
    if button.value == True:
        break
    led1.value = False
    time.sleep(.5)
    if button.value == True:
        break

if var == 0:
    print ("liftoff")
    led2.value = True
    time.sleep(5)
    led2.value = False