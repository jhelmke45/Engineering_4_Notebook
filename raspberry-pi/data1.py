import board
import time
import adafruit_mpu6050
import busio
import digitalio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)   # i2c setup

led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT  # add LED

onboard = digitalio.DigitalInOut(board.LED)
onboard.direction = digitalio.Direction.OUTPUT  # onboard LED for mode indication

mpu = adafruit_mpu6050.MPU6050(i2c)     # accelerometer

tilt = 0

with open("/data.csv", "a") as datalog:     # define datalog

    while True:
        x = mpu.acceleration[0]
        y = mpu.acceleration[1]
        z = mpu.acceleration[2]
        t = time.monotonic()

        print(f"Time: {t}   X: {x:.3f}   Y: {y:.3f}   Z: {z:.3f}")
        if mpu.acceleration[2] < 0:     # light on if tilted more than 90 degrees
            led.value = True
            tilt = 1
        else:
            led.value = False
            tilt = 0
        
        datalog.write(f"{t},{x},{y},{z},{tilt}\n")      # create data columns for time, tile, and each axis
        datalog.flush()
        onboard.value = True
        time.sleep(.15)
        onboard.value = False
        time.sleep(.1)
                                                                                                      