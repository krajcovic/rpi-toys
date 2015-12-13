#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from subprocess import call
from firebase import firebase
import time

fbApp = firebase.FirebaseApplication('https://angular-template.firebaseio.com/', None)

def postTemperature(temperature):
    result = fbApp.post('/thermals', {'thermal_zone0': temperature, 'timestamp' : time.time()})
    print(result)

def getTemperature():
    #return call(["cat", "/sys/class/thermal/thermal_zone0/temp"])
    zone = open('/sys/class/thermal/thermal_zone0/temp')
    return zone.read()

def main():
    #print(getTemperature())
    postTemperature(getTemperature())


if __name__ == "__main__":
    main()