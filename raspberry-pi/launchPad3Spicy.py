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

while True:
    if button.value == True:
        var = 10

        for x in range (10):
            print(10-x)
            var = x
            led1.value = True
            time.sleep(.5)
            while button.value == True:
                if button.value == False:
                    print("ABORT")
                    break

            led1.value = False
            time.sleep(.5)
            while button.value == True:
                if button.value == False:
                    print("ABORT")
                    break

        if var == 0:
            print ("liftoff")
            led2.value = True
            time.sleep(5)
            led2.value = False
            break