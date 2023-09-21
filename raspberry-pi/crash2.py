import board
import time
import adafruit_mpu6050
import busio
import digitalio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print(f"X: {mpu.acceleration[0]:.3f}   Y: {mpu.acceleration[1]:.3f}   Z: {mpu.acceleration[2]:.3f}")
    if mpu.acceleration[2] < 0:
        led.value = True
    else:
        led.value = False