import board
import time
import adafruit_mpu6050
import busio
import digitalio
from adafruit_display_text import label     # OLED imports
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)   # i2c setup

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP1)   # OLED adress 0x3d
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)   # accelerometer 0x68

splash = displayio.Group()  # create splash
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)


while True:
    print(f"X: {mpu.gyro[0]+.01:.3f}   Y: {mpu.gyro[1]-.019:.3f}   Z: {mpu.gyro[2]+.028:.3f}")  # displayed values manually adjusted for error
    if mpu.acceleration[2] < 0:
        led.value = True
    else:
        led.value = False
    text_area.text = f"X: {mpu.gyro[0]+.01:.3f}\nY: {mpu.gyro[1]-.019:.3f}\nZ: {mpu.gyro[2]+.028:.3f}"  # send text to OLED
    time.sleep(.25)