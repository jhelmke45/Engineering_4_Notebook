import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT  # LED setup

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier      # preset delay times

while True:
    string = input("Enter message, or '-q' to quit: ")
    if string == '-q':
            break
    string = string.upper()
    temp = ""
    for x in range(len(string)):        # loop through each character
        temp += MORSE_CODE[string[x]] + " "
    print(f"{temp} ")
    for y in temp:
        if y == '.':
            led.value = True
            time.sleep(dot_time)    # dot delay
            led.value = False
        if y == '-':
            led.value = True
            time.sleep(dash_time)   # dash delay
            led.value = False
        if y == ' ':
            time.sleep(between_letters) # letter delay
        if y == '/':
            time.sleep(between_words)   # space delay
        time.sleep(between_taps)    # add on default delay