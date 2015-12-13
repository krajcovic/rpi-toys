#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'


import getopt
import sys
import urllib
import json
import calendar
import time
import datetime
from subprocess import call
from firebase import firebase
from bson import json_util



#device = "wlan0"
#temp = "wifistat.out"

class WifiState():

    def __init__(self, state):
        self.device = "wlan0"
        self.timestamp = time.time()
        self.timestamp_formated = datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')
        self.state = state

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)



def saveWifiStat(device, outputFileName):
    #retcode = call("date > {0}".format(outputfilename), shell=True)
    retcode = call("iwconfig {0} > {1}".format(device, outputFileName), shell=True)

def printWifiStat(outputFileName):
    fileWifiStat = open(outputFileName, "r")
    print(fileWifiStat.read())

def getWifiStat(outputFileName):
    fileWifiStat = open(outputFileName, "r")
    return fileWifiStat.read()

def firebaseSendData(outputFileName):
    # url = 'https://mycooltemperatureapp.firebaseio.com/readings.json'
    # postdata = {
    #     'date': str(calendar.timegm(time.gmtime())),
    #     'wifistat': str(getWifiStat(outputFileName))
    # }
    # print(postdata)

    fb = firebase.FirebaseApplication('https://shining-torch-4771.firebaseio.com/', None)

    new_user = 'Ozgur Vatansever'
    wifistate = WifiState(getWifiStat(outputFileName))
    result = fb.post('/wifistate', wifistate.to_JSON()) # {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'}

def usage():
    """ Print info about using iwconfig.py. """
    print("""Usage: wifistat.py [interface]
       Check man pages for more details.""")

def version_info():
    """ Print version info for iwconfig.py, Wireless Extensions compatibility,
        and Wireless Extensions version in the kernel.
    """
    pass

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "version"])
    except getopt.GetoptError as error_str:
        # invalid option will be taken to be interface name
        pass
    else:
        try:
            if opts[0][0] in ("-h", "--help"):
                usage()
        except

    saveWifiStat("wlan0", "wifistat.out")
    firebaseSendData("wifistat.out")
    #printWifiStat(outputfilename)

if __name__ == '__main__':
    main()




