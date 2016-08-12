import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)     #Define pin 3 as an output pin

def check_distance(time):
    SPEED = 17.150
    return SPEED * time

print check_distance(30)

def light_it_up():
    distance = check_distance(30)
    if distance > 100:
        GPIO.output(3,1)
    else:
        GPIO.output(3,0) 


light_it_up() 

