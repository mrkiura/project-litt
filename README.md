# project-litt
A solution to automatically control lights based on light levels and movement.

##Requirements
####Hardware
+ Raspberry pi (2 Model B)
+ USB Keyboard
+ LED
+ Jumper wires
+ 3 - 10k resistors, 1 - 1k resistor
+ Ultrasonic sensor hc-sr04
+ Breadboard

####Software
+ Raspbian (OS)
+ Text editor (VIM)
+ Python
+ RPI.GPIO module

##Instructions
+ Install the [Raspbian] (https://www.raspberrypi.org/downloads/raspbian/) operating system. 
+ Install the text editor on the OS
+ Install Python
+ Clone this repo `git clone git@github.com:andela-akiura/project-litt.git`
+ Install the RPI.GPIO module
+ Connect the jumper wires as shown in the diagram
+ Run the program `python demo.py`

##Description
> When it is past 1800hrs and before 0700hrs, the motion sensor detects movement and sends a signal. The time difference between the trigger and echo is recorded. 
> The distance between the obstacle and the sensor is calculated by ```distance = speed * time/2``` where `speed` is the speed of sound `340.29 m / s` 
> If the distance between the obstacle and motion sensor is within the range, the bulb lights, otherwise the bulb goes off.
