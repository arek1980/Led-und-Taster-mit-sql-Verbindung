import RPi.GPIO as GPIO
import time
   
LED = 37
   
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)   
print("Hallo Welt")
   
try:
	while True:
		GPIO.output(LED, True) # LED an
		print("blink")
		time.sleep(0.5)
		GPIO.output(LED, False) # LED aus
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
