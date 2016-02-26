import RPi.GPIO as GPIO
import sys
from ConfigParser import SafeConfigParser

# CONSTANTS
#PIN_OUTPUT_1 = 9 # I think
PIN_OUTPUT_2 = 11
PIN_OUTPUT_3 = 13
PIN_OUTPUT_4 = 15

# There are 4 outputs connected to relays, labelled #1-4. #1 appears to be broken
def output(output_num, action):
	if action  == 'on':
		state = GPIO.HIGH
	elif action == 'off':
		state = GPIO.LOW
	else:
		print "Invalid action. Must be either 'on' or 'off'"
		sys.exit()


	if output_num == 1:
		print "Output #1 is broken."
		sys.exit()
	elif output_num == 2:
		GPIO.output(PIN_OUTPUT_2, state)
	elif output_num == 3:
		GPIO.output(PIN_OUTPUT_3, state)
	elif output_num == 4:
		GPIO.output(PIN_OUTPUT_4, state)
	else:
		print "Invalid output #"
		sys.exit()
	

def init():
	# Avoid warnings 
	GPIO.setwarnings(False)

	# to use Raspberry Pi board pin numbers
	GPIO.setmode(GPIO.BOARD)

	# Set up relevant GPIO channels
	#GPIO.setup(PIN_OUTPUT_1, GPIO.OUT)
	GPIO.setup(PIN_OUTPUT_2, GPIO.OUT)
	GPIO.setup(PIN_OUTPUT_3, GPIO.OUT)
	GPIO.setup(PIN_OUTPUT_4, GPIO.OUT)

