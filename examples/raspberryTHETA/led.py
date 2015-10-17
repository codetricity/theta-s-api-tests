import RPi.GPIO as GPIO
import time
from thetapylib import *

led_pin = 25
switch_pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_state = 0

try:
	while True:
		#GPIO.output(led_pin, True)
		#time.sleep(0.5)
		GPIO.output(led_pin, True)
		#time.sleep(0.5)
		# if not GPIO.input(switch_pin):
		# 	print("Button pressed")
		# 	if led_state == 0:
		# 		led_state = 1
		# 	else:
		# 		led_state = 0
		# 	sid = startSession()
		# 	takePicture(sid)
		# 	time.sleep(0.8)
	
		# print(led_state)
	

finally:
	print("Cleaning up")
	GPIO.cleanup()
