import board
import time
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle   # import shapes for OLED

displayio.release_displays()

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)   # OLED i2c

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()
title = " "
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

hline = Line(64,0,64,64, color=0xFFFF00)    # center lines
splash.append(hline)
hline = Line(0,32,128,32, color=0xFFFF00)
splash.append(hline)

circle = Circle(64, 32, 5, outline=0xFFFF00)    # center circle
splash.append(circle)
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0

# triangle = Triangle(-10, 6, -54, 19, -60, -30, outline=0xFFFF00) # test
# splash.append(triangle)

def tri (set1, set2, set3): # function to return area
    try:
        set1 = set1.split(",")
        set2 = set2.split(",")
        set3 = set3.split(",")

        x1 = float(set1[0])
        y1 = float(set1[1])
        x2 = float(set2[0])
        y2 = float(set2[1])
        x3 = float(set3[0])
        y3 = float(set3[1])

        area = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)    # formula for triangle area

        return area

    except:
        print("invalid input, try again")   # return -1 if coordinate invalid, and return to input sequence
        area = -1
        return area

while True:
    input1 = input("input coordinate 1: ")      # input for 3 coordinates
    input2 = input("input coordinate 2: ")
    input3 = input("input coordinate 3: ")

    a = tri(input1, input2, input3)     # get area from function

    if(a >= 0):
        print(f"area: {a}")
        triangle = Triangle(int(x1+64), int(-y1+32), int(x2+64), int(-y2+32), int(x3+64), int(-y3+32), outline=0xFFFF00) # print triangle with adjustments for center
        splash.append(triangle)

