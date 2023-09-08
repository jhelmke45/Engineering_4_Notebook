import board
import digitalio
import time
import pwmio
from adafruit_motor import servo

led1 = digitalio.DigitalInOut(board.GP1)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP3)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0

while button.value == False:
    print('ready for liftoff')

for x in range (10):
    print(10-x)
    led1.value = True
    time.sleep(.5)
    led1.value = False
    time.sleep(.5)

print ("liftoff")
led2.value = True
servo1.angle = 180
time.sleep(5)
led2.value = False