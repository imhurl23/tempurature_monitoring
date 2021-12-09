
#Izzy Hurley
#cs431 networks
#12/2/21
#awknowledgement: elements adapted from elements of aws publishing code
#purpose: read sensors and parse results to be sent 

# importing libraries
import glob
import time
import os
import sys
import json
from datetime import datetime

#  An Example Reading from /sys/bus/w1/devices/<ds18b20-id>/w1_slave
#  a6 01 4b 46 7f ff 0c 10 5c : crc=5c YES
#  a6 01 4b 46 7f ff 0c 10 5c t=26375

import RPi.GPIO as GPIO

#  Set Pullup mode on GPIO first.
GPIO_PIN_NUMBER=14
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO_PIN_NUMBER=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def ds18b20_read_sensors():
  rtn = {}
  w1_devices = []
  w1_devices = os.listdir("/sys/bus/w1/devices/")
  for deviceid in w1_devices:
    rtn[deviceid] = {}
    rtn[deviceid]['temp_c'] = None
    device_data_file = "/sys/bus/w1/devices/" + deviceid + "/w1_slave"
    if os.path.isfile(device_data_file):
      try:
         f = open(device_data_file, "r")
         data = f.read()
         f.close()
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

def ot_readings():
  now = datetime.now()
  print(datetime.now())
  day = now.strftime("%D")
  curr_time = now.strftime("%H:%M:%S")
  curr_time = curr_time[:-3]

  temp_readings = ds18b20_read_sensors()
  temp_read = {}
  temp_read['day'] = day
  temp_read['timestamp'] = curr_time
  #device iterator for labeling
  di = 0
  for t in temp_readings:
#     print(t)
    if t[0] == '2':
        di +=1
        device_name = "device_" + str(di)
        temp_read[device_name] = temp_readings[t]['temp_c']
#         print(temp_readings[t]['temp_c'])
        if 'error' in temp_readings[t]:
          temp_readings = ds18b20_read_sensors()
        
  print (temp_read)
  return temp_read
    
def readtojson():
 temps = []
 while True:
  temp_readings = ds18b20_read_sensors()
  print(temp_readings)

  for t in temp_readings:
    if not 'error' in temp_readings[t]:
      #print(u"Device id '%s' reads %.3f +/- 0.5 °C" % (t, temp_readings[t]['temp_c']))
      datpt = {
        "device" : t,
        "temp" : temp_readings[t]
          }
      temps.append(datpt)

   
 
#  with open('out_temps.json', 'a') as f:
#      json.dump(temps,f,indent =4)


      
if __name__ == '__main__':
    ot_readings()
