import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG = 23
ECHO = 24
LED_PIN = 3

MIN_DISTANCE = 10
MAX_DISTANCE = 300

print "Distance Measurement In Progress"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(TRIG, False)

print "Waiting For Sensor To Settle"
time.sleep(2)

while True:
    current_time = time.localtime(time.time()).tm_hour
    if current_time >= 7 and current_time <= 18:  
        GPIO.output(TRIG, True)
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input (ECHO)==0:
            pulse_start = time.time()

        while GPIO.input (ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)
    
        if distance > MIN_DISTANCE and distance < MAX_DISTANCE:
            GPIO.output(LED_PIN,1)
        else:
            GPIO.output(LED_PIN,0)
       
        print "Obstacle is ", distance, "cm away."
    else:
        GPIO.output(LED_PIN, 0)

GPIO.cleanup() 
