import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_PIN = 3 #Define pin 3 as an output pin
TRIG = 23 # Associate pin 23 to TRIG
ECHO = 24 # Associate pin 24 to ECHO

GPIO.setup(LED_PIN,GPIO.OUT) 
   
def check_distance(time):
    SPEED = 17.150
    return SPEED * time

print check_distance(30)

def light_it_up():
    distance = check_distance(30)
    if distance > 100:
        while True:
            GPIO.output(LED_PIN,1)
            time.sleep(1)
            GPIO.output(LED_PIN, 0)
            time.sleep(1)
    else:
        GPIO.output(LED_PIN,0) 


light_it_up() 

