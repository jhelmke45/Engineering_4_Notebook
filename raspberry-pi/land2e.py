# This code is taken from Elias Garcia

import time
import board
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
displayio.release_displays()


sda_pin = board.GP14                                # These set up the oled board
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 
display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP0) 
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def total_area (set1, set2, set3):
    try:
        set1 = set1.split(',')                       #splits each ordered pair at the comma
        set2 = set2.split(',')
        set3 = set3.split(',')

        x1 = float(set1[0])                          #assigns each x and y value to its own separate float
        y1 = float(set1[1])
        x2 = float(set2[0])
        y2 = float(set2[1])
        x3 = float(set3[0])
        y3 = float(set3[1])

        area = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))*.5)           #formula for area of ordered pair triangle
        splash = displayio.Group()
        print(f"\nThe area of the triangle with the coordinates ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) is {area} km squared")
        hline = Line(0,32,128,32, color=0xFFFF00)                  #x axis line
        splash.append(hline)
        vline = Line(64,64,64,0, color=0xFFFF00)                   #y axis line
        splash.append(vline)
        triangle = Triangle(int(x1+64), int(-y1+32), int(x2+64), int(-y2+32), int(x3+64), int(-y3+32), outline=0xFFFF00)
        splash.append(triangle)
        title = f"Area: {area}"
        text_area = label.Label(terminalio.FONT, text = title, color = 0xFFFF00, x = 5, y= 5)
        splash.append(text_area)
        display.show(splash)    
        
        return area

    except:
        print("These points are invalid, try again")                #if invalid retry

while True:
    in1 = input("Enter the first (x,y) coordinate")                 #input prompts
    in2 = input("Enter the second (x,y) coordinate")
    in3 = input("Enter the third (x,y) coordinate")

    areaA = total_area(in1, in2, in3)
    
    if areaA == 0:
        continue
    else:
        print(f"The area of the triangle with verticies ({in1}), ({in2}), ({in3}) is {areaA} square km.")           #returm statement