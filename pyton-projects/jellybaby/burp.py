#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import time
import RPi.GPIO as GPIO
import os
import threading


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN)
print("Press control button")
while True:
    if GPIO.input(4) == False:
        os.system("omxplayer burp.wav")
        time.sleep(1)



