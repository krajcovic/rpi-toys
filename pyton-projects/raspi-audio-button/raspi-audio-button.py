#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

# while True:
if (GPIO.input(23) == False):
    os.system('mpg123 -q artic_monkeys_-_mardy_bum.mp3 &')

if (GPIO.input(24) == False):
    os.system('mpg123 -q artic_monkeys_-_mardy_bum.mp3 &')

if (GPIO.input(25)== False):
    os.system('mpg123 -q artic_monkeys_-_mardy_bum.mp3 &')

sleep(1);