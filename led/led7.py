import RPi.GPIO as GPIO # Import GPIO library

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
