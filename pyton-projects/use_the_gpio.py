#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import RPi.GPIO as GPIO
import time

PIN = 17
TIMEOUT = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN,1)

time.sleep(TIMEOUT)

GPIO.output(PIN,0)

time.sleep(TIMEOUT)

GPIO.output(PIN,1)

time.sleep(TIMEOUT)

GPIO.output(PIN,0)

print('Done')
GPIO.cleanup()
