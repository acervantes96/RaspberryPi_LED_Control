import RPi.GPIO as GPIO
import time

# Setting GPIO mode
GPIO.setmode(GPIO.BCM)

# Defining the pins for LEDs
led_1 = 17
led_2 = 18

# Setting up GPIO pins and outputs
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)

try:
    while True:
        # Turn LED 1 ON
        GPIO.output(led_1, GPIO.HIGH)
        print("LED 1 is ON")
        time.sleep(0.5) # ON for 0.5s

        #Turn LED 1 OFF
        GPIO.output(led_1, GPIO.LOW)
        print("LED 1 is OFF")
        time.sleep(0.5) # 0.5s wait

        # Turn LED 2 ON
        GPIO.output(led_2, GPIO.HIGH)
        print("LED 2 is ON")
        time.sleep(0.5) # ON for 0.5s

        # Turn LED 2 OFF
        GPIO.output(led_2, GPIO.LOW)
        print("LED 2 is OFF")
        time.sleep(0.5) # 0.5s wait

except KeyboardInterrupt:
    # Clean exit when Ctrl+C is pressed
    GPIO.cleanup()
