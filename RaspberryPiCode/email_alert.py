#Izzy Hurley
#11/29/21
#adopted parts from AWS IOT sdk files 
#purpose: file to read temps and send alerts on extranious values

import glob
import time
import os
import sys
from email2 import  sendAlert
#  An Example Reading from /sys/bus/w1/devices/<ds18b20-id>/w1_slave
#  a6 01 4b 46 7f ff 0c 10 5c : crc=5c YES
#  a6 01 4b 46 7f ff 0c 10 5c t=26375

import RPi.GPIO as GPIO

 

def ds18b20_read_sensors():
  #function to read from the tempurature sensors
  rtn = {}
  w1_devices = []
  #access sensor directory
  w1_devices = os.listdir("/sys/bus/w1/devices/")
  for deviceid in w1_devices:
    rtn[deviceid] = {}
    rtn[deviceid]['temp_c'] = None
    #set and check file data
    device_data_file = "/sys/bus/w1/devices/" + deviceid + "/w1_slave"
    if os.path.isfile(device_data_file):
      try:
	 #open and read the file
         f = open(device_data_file, "r")
         data = f.read()
         f.close()
         #if data found then parse
         if "YES" in data:
           (discard, sep, reading) = data.partition(' t=')
           rtn[deviceid]['temp_c'] = float(reading) / float(1000.0)
         else:
           rtn[deviceid]['error'] = 'No YES flag: bad data.'
      except Exception as e:
         rtn[deviceid]['error'] = 'Exception during file parsing: ' + str(e)
    else:
      rtn[deviceid]['error'] = 'w1_slave file not found.'
  return rtn;
#continually record temps until pi turned off
while True:
 temp_readings = ds18b20_read_sensors()
 temps = []
 #for number of configured devices
 
 # if not 'error' in temp_readings[t]:
 # print(u"Device id '%s' reads %.3f +/- 0.5 °C" % (t, temp_readings[t]['temp_c']))
 if  temp_readings['28-3c01e076ca6e']['temp_c'] == None:
    continue #don't email on false recordings
 temps.append(int(temp_readings['28-3c01e076ca6e']['temp_c']))
 #allow user to configure email 
 email = input("please enter an email to recieve messages:")
 sendAlert(email,temps[0],30)
 #wait for 5 minutes 
 time.sleep(300)

