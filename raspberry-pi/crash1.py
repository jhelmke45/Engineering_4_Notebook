import board
import time
import adafruit_mpu6050
import busio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)   # i2c setup

mpu = adafruit_mpu6050.MPU6050(i2c)     # connect accelerometer

while True:
    print(f"X: {mpu.acceleration[0]:.3f}   Y: {mpu.acceleration[1]:.3f}   Z: {mpu.acceleration[2]:.3f}")    # format outputs to 3 decimals