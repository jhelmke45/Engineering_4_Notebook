[data.csv](https://github.com/jhelmke45/Engineering_4_Notebook/files/14040560/data.csv)# Engineering_4_Notebook

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
* [Beam_2](#Beam_2)
* [Beam_3](#Beam_3)
* [Landing_Area_1](#Landing_Area_1)
* [Landing_Area_2](#Landing_Area_2)
* [Morse_Code_1](#Morse_Code_1)
* [Morse_Code_2](#Morse_Code_2)
* [Data_1](#Data_1)
* [Data_2](#Data_2)
  

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

In this assignment I connected an accelerometer to the Pico, and printed data from it onto the serial monitor.

### Evidence

### Wiring

![Accelerometer1 wiring](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/d6e54537-ffd4-4350-9d70-7a380f673acc)

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/crash1.py)

### Reflection

This assignment wasn't too hard, but was a reasonable introduction to the workings of i2c. It was also good practice with f-strings, which I used to print the variables and format the decimals. 

## Crash_Avoidance_2

### Description

In this assignment I made use of the accelerometer to turn on an LED when the breadboard is tilted past 90 degrees. The module can also now be disconnected from the computer and powered with a battery.

### Evidence

https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/c0ff3762-131c-401b-8245-428276fb442e

### Wiring

![Accelerometer2 wiring](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/567fca03-5875-49db-91aa-07ff5e39ee27)

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/crash2.py)

### Reflection

The code on this assignment wasn't too hard, but did take some logic. To tell if the board was tilted past 90 degrees, I took advantage that gravity applies a constant downwards acceleration. Because of this, if the Z (vertical) acceleration if less than zero, the board must be tilted so that gravity is either having no affect because it's sideways, or is negative because it's upside down. The baterry was also a nice touch, and the whole finished product feels more complete when you can disconnect it from the computer and it still works like normal.

## Crash_Avoidance_3

### Description

In this assignment I added an OLED screen to the accelerometer which prints out angular velocity.

### Evidence

https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/9e51b337-f006-4da7-bb83-d6b3c2de65c6

### Wiring

![Accelerometer3](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/d7493389-980c-42d6-91b2-6c700090137b)

### Code

[Code link](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/crash3.py)

### Reflection

This assignment was definitely a step up from the others. The OLED was relatively straightforward since we didn't do anything complicated with it, but I did have to do some troubleshooting to figure out all of the commands. The thing that gave me the most trouble was figuring out the i2c system, although part of that ended up being a dead OLED. Switching to angular velocity instead of acceleration was simply a matter of changing the built in command.

## Beam_1

### Assignment Description

This was the first section of our beam assignment, the goal being to design and mock up a beam that could hold as much weight ( 180mm from the lever point ) as possible without snapping or excessive deflecting, while maintaining a weight below 13g.

### Part Link

[Link to our Onshape document](https://cvilleschools.onshape.com/documents/bbb8fb04f2c7e9a26ef00d6f/w/8353d61f44a10197441fa346/e/12a872e8fa7823561546f9c6)

### Part Image

![Beam Image](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/beam.PNG)

### Reflection
Like many other groups, we began by reasearching [beam theory](https://en.wikipedia.org/wiki/Euler%E2%80%93Bernoulli_beam_theory#:~:text=Euler%E2%80%93Bernoulli%20beam%20theory%20), a study of how load bearing beams behave elastically and deflect. We then looked into succesful cantilever beam designs, as well as commonplace beam designs that are very prevalent, such as I-Beams ( simillar to the design we ended up going with ). We then began to design our beam using ideas we had gathered, an I-Beam adjacent design with a strong load bearing top section with 45&deg; chamfers to increase strength and printability constraints of the assignment. Other strategic design choices we made include, a thin middle section, as well as holes along the middle and bottom, to reduce mass on a relatively low load bearing components. We also had to make sure that there were no vertical angles above 45&deg; as that was one of our design constraints due to the printer only being able to print up to 45&deg;. Lots of thanks to [Komaram Bheem](https://en.wikipedia.org/wiki/Komaram_Bheem?scrlybrkr=973947e4) for help with the pronunciation and etymology of his name, as well as help with certain aspects of our design.

&nbsp;

## Beam_2

### Assignment Description
For this assignment we built upon our first beam design using Onshape's built in FEA analysis software to determine areas of high stress and displacement in order to edit our design to account for these flaws in our first design.

### Part Link

[Link to our Onshape document](https://cvilleschools.onshape.com/documents/bbb8fb04f2c7e9a26ef00d6f/w/8353d61f44a10197441fa346/e/12a872e8fa7823561546f9c6)

### Part Image
_All simulations tested with 30N of force_
![Beam Stress](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/stress.PNG)
_FEA sim of stress -- Max stress around 80MPa_

![Beam Safety](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/saftey.PNG)
_FEA sim of safety factor -- Min around .4_

![Beam Displacement](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/displace.PNG)
_FEA sim of displacement -- Max around 50mm_

### Reflection
After running the FEA simulation for our initial beam design, we were able to visualise the areas of our beam under the most stress as well as areas most likely to break. As shown in the above images, the part of the top rail nearest the base, as well as the area nearest the weight seem to be the areas under the most stress. In order to strengthen these parts and better distribute the stress, we will be removing material from areas with the littlest stress and adding it to these areas. For example, we could remove material from the center of the upper rail as well as the area closest to the weight under the least stress and add it to the areas described above. The FEA simulation tools in onshape are relatively complete and fairly simple to use, so after running through the short training activities I felt like I had a good grasp on the simulation tools, although, when first testing our beam, we diddn't add a bearing face, so we got unrealistic results (we were able hold >20 lbs of force), but once we fixed that we were able to easily analyze the forces acting on our beam.

&nbsp;

## Beam_3

### Assignment Description
For this section of the beam assignment we first improved our design based on the Onshape FEA simulation, and then tested the improved design in the real world giving us much more accurate results allowing us to iterate on our design once again with accurate, real world data.

### Part Link

[Link to our Onshape document](https://cvilleschools.onshape.com/documents/bbb8fb04f2c7e9a26ef00d6f/w/8353d61f44a10197441fa346/e/12a872e8fa7823561546f9c6)

### Part Image

![Beam2 Stress](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/stress%202.png)
_FEA sim of stress 2nd iteration (MPa)_

![Beam3 Stress](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/stress%203.png)
_FEA sim of stress 3rd iteration (MPa)_

![Beam2 Displacement](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/displacement%202.png)
_FEA sim of displacement 2nd iteration_

![Beam3 Displacement](https://github.com/egarcia28/Engineering_4_Notebook/blob/main/images/displacement%203.png)
_FEA sim of displacement 3rd iteration_


### Reflection
When it came to improving our design based on our first FEA simulation, we just added some simple changes to better distribute the stress. These changes include, removing material from the sides by connecting the holes together, and adding that material to the top rail near the base and weight through some simple chamfers and extrusions. When we tested this in the real world we did pretty well and held a decent ammount of weight, but our beam ultimately broke due to the lack of support on the sides created by the singular long hole, causing it to bend sideways and break much quicker. When we went back to Onshape to improve our design from the real world results, we re-connected all of the holes to add support and prevent the beam from twisting, we also added a secondary rail on the top in order to better distribute the stress. When testing our 3rd iteration in the real world it held much more weight and diddn't twist, when it finally broke it shattered showing that we had done a pretty good job of distributing the stress.  
&nbsp;

## Landing_Area_1

### Description

In this assignment I made a program that takes 3 coordinate sets as an input, and outputs the area of the triangle between them.

### Evidence

![land1-ezgif com-optimize](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/d269658c-7caf-4e70-8dc6-eb78b17384cf)

### Code

https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/land.py

### Reflection

This assignment was relatively straightforward, but there were some new python components that we haven't really used before. This program took advantage of a funtion for the triangle solver, as well as using the ``` input() ``` command, both of which I don't think we've had in an assignment before. The actual solving of the triangle area was simply a matter of putting the variables into an equation and returning it.

## Landing_Area_2

### Description

In this assignment I added on to the previous triangle program by making it print the points and triangle onto a graph displayed on an OLED screen.

### Evidence

![land2-ezgif com-video-to-gif-converter](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/a303ccda-9c8c-4d45-b62c-c29421fb4a64)

### Wiring

![landingareawiring](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/a80e7b84-f66b-4413-bb1a-c7d45bd4235f)

_diagram by [Elias](https://github.com/egarcia28/Engineering_4_Notebook/tree/main?tab=readme-ov-file#Raspberry_Pi_Landing_Area_2), who I worked with on this assignment_

### Code

https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/land.py

### Reflection

Using the OLED screen was fun, as it's a lot more customizable than something like an LCD. I didn't have much trouble printing the lines and circle, but for whatever reason my triangle command would not work, no matter what I tried. I tried [Elias'](https://github.com/egarcia28/Engineering_4_Notebook/tree/main?tab=readme-ov-file#Raspberry_Pi_Landing_Area_2) code and it seemed to solve the problem, but I still can't find what's so different with mine. 

## Morse_Code_1

### Description

In this assignment I made a program that takes text as an input, translates it to morse code, and prints the morse code version.

### Evidence

![morse1-ezgif com-optimize](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/30a6d7c3-a47b-4a96-9adc-92921c4fc1b7)

### Code

https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/morse1.py

### Reflection

I like the more code-heavy assignments, so this one was fun for me. We were conveniently given a dictionary with all of the morse code traslations, so a lot of time was saved by not having to do it manually. I used a ``` for ``` loop to loop through each character in the input string and translate them to morse code, and then add them to a seperate string. 

## Morse_Code_2

### Description

In this assignment I added on to the morse code translator by making it blink an LED as the output, with different delays for dots, dashes, spaces, and word breaks.

### Evidence

![morse2-ezgif com-optimize](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/556b32a7-82c9-49fe-a29c-98de6a1aad5e)

### Wiring

![morsecode2wiring](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/cf259f70-b9fb-427b-a1f9-6ac87423c567)

_diagram by [Elias](https://github.com/egarcia28/Engineering_4_Notebook/tree/main?tab=readme-ov-file#Raspberry_Pi_Morse_Code_2), who I worked with on this assignment_

### Code

https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/morse2.py

### Reflection

We were given the ideal delay values, so this assignment was mostly a matter of connecting an LED and implementing the different delays. To do this, I added a loop to the end that loops through the final morse string, and then delays and blinks according to what character it sees. 

## Data_1

### Description

In this assigment, I had a battery-powered Pico collect and store data from an accelerometer, before transfering onto the computer in the form of a spreadsheet.

### Evidence

[Data spreadsheet](https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/data.csv)

### Wiring

![Accelerometer2 wiring](https://github.com/jhelmke45/Engineering_4_Notebook/assets/113116262/0a413df7-26e6-4c03-9d2a-ecc7560c0879)

_Wiring diagram from [Elias](https://github.com/egarcia28/Engineering_4_Notebook/tree/main?tab=readme-ov-file#Raspberry_Pi_Data_Storage_1), who I worked with on this assignment_

### Code

https://github.com/jhelmke45/Engineering_4_Notebook/blob/main/raspberry-pi/data1.py

### Reflection

For this assignment I had to distinguish between "code mode" and "data mode" for the Pico. I had to change the ```boot.py``` file

## Data_2

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[Link to notebook](https://github.com/jhelmke45/Engineering_4_Notebook/tree/main)

### Test Image

![turtle](images/turdle.png)

### Test GIF

![yum](images/yum.gif)
