# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch_Pad_1](#Launch_Pad_1)
* [Launch_Pad_2](#Launch_Pad_2)
* [Launch_Pad_3](#Launch_Pad_3)
* [Launch_Pad_4](#Launch_Pad_4)
* [Crash_Avoidance_1](#Crash_Avoidance_1)
* [Crash_Avoidance_2](#Crash_Avoidance_2)
* [Crash_Avoidance_3](#Crash_Avoidance_3)
* [Beam_1](#Beam_1)
  

&nbsp;

## Launch_Pad_1

### Assignment Description

In this assignment, I used the serial monitor to count down from 10, simulating the countdown to liftoff for a rocket. It counts down each socend, and then displays "liftoff" at the end of the run.

### Evidence 

https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/9c988bc3-e03a-46a8-9d17-9b6c1713b339 

### Code

[Link to code](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/launchPad1)

### Reflection

This assignment was pretty straightforward, but a good introduction to the picos, and a way to get readjusted to VS code. I had also never used a ```for``` loop in python, so that will definitely be useful to know in the future. 

&nbsp;

## Launch_Pad_2

### Description

In this assignment I added on to the countdown by making a red light flash on each count. Additionally, a green light turns on for a few seconds when liftoff occurs.

### Evidence

https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/8163db1a-beec-4597-b05a-54625cc7ab7f

### Wiring

![IMG-2678](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/25332870-f331-473f-a9d9-bf9bfaf81de3)

_Wiring diagram from [Elias](https://github.com/egarcia28/Engineering_4_Notebook), mine is the same because we worked together_

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/launchPad2)

### Reflection

This assignment was also pretty simple, but was a good refresher on using LEDs. It was also a good way to get used to the pin layout of the Pico. There wasn't too much to change in the code, except making the LED blinks part of the normal delay.

&nbsp;

## Launch_Pad_3

### Description

In this assignment I further added to the countdown by having the monior print "ready for liftoff" until a button is pressed. Then, the countdown plays out like before.

### Evidence

https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/dc3d7ff6-8a32-4b47-86e9-89ed50d6b333

### Wiring

![IMG-2679](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/90b27613-7af4-4e30-a885-179b9a9070e6)

_Diagram from [Elias](https://github.com/egarcia28/Engineering_4_Notebook), we worked together again_

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/launchPad3.py)

### Reflection

I sort of did the spicy version of this assignment by making the run abort when the button is pressed, but it does not continue to run. This was the first component that we used that is implemented differently with the Pico, but it wasn't too much of a challenge because the Pico made using the button easier. The only thing that was potentially confusing was the difference between pulling the button up or down, but again it wasn't very hard to figure out.

&nbsp;

## Launch_Pad_4

### Description

In this assignment, I added on to the launch sequence by making a servo rotate 180 degrees at the end of the sequence, simulating a tower disconnecting from the rocket before launch. The servo starts retracting 3 seconds before launch, and reaches 180 as it launches.

### Evidence

https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/d86452d1-b964-48e0-8b8e-269d314eca53

### Wiring

![IMG-2680](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/3420bda8-4b5b-4d88-b1cc-782c8170d9c8)

_Wiring from [Elias](https://github.com/egarcia28/Engineering_4_Notebook), my servo is on GP0 instead of GP4_

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/launchPad4Spicy.py)

### Reflection

I did the spicy version for this assignment by making a seperate ```for``` loop for the last 3 seconds, and having the servo rotate 3 degrees by a time. Using a servo with the Pico was pretty straightforward, and I dont think there were any changes from the Metro. 

&nbsp;

## Crash_Avoidance_1

### Description

### Evidence

### Wiring

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/crash1.py)

### Reflection

## Crash_Avoidance_2

### Description

### Evidence

### Wiring

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/crash2.py)

### Reflection

## Crash_Avoidance_3

### Description

### Evidence

### Wiring

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/crash3.py)

### Reflection

## Beam_1

### Assignment Description

In this assignment my partner [Elias](https://github.com/egarcia28/Engineering_4_Notebook) and I began designing a beam, with the goal of holding as much weight as possible on one end. The weight will be placed 180mm from the base, and the beam cannot weigh more than 13 grams. There are also some requirements, such as no angles being more than 45 degrees, which are in place to simplify 3D printing. 

### Part Link 

[Onshape Link](https://cvilleschools.onshape.com/documents/bbb8fb04f2c7e9a26ef00d6f/w/8353d61f44a10197441fa346/e/12a872e8fa7823561546f9c6?renderMode=0&uiState=651d7c84c8b5ae0b47f2d3a3)

### Part Image

![beam](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/f2bcce92-0afd-49b4-8c0c-c87431edaf0e)

### Reflection

Before even beginning to model, we did some research into "beam theory," and the general behavior of beams when put under stress. This helped us understand what the beam would do when a load was placed on the end, and predict what could go wrong. We ended up modeling ours to be similar to an I beam, with a sloped end. This should hopefully mean that we have a strong base which can distribute weight evenly. To cut down the weight we thinned out the middle section and added a bunch of holes in spots we thought could take the extra stress. 

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[Link to notebook](https://github.com/jhelmke45/Engineering_4_Notebook/tree/main)

### Test Image

![turtle](images/turdle.png)

### Test GIF

![yum](images/yum.gif)
