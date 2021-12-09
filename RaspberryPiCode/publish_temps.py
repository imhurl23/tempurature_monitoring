#Izzy Hurley
#cs431 networks
#12/2/21
#awknowledgement: elements adapted from elements of aws publishing code
#purpose: leverage mqtt protocol to send temps to aws IoT core 



# importing libraries
import paho.mqtt.client as paho
import os
import socket
import ssl
import random
import string
import json
from returntemp import ot_readings
from time import sleep

from random import uniform
 
connflag = False
 
def on_connect(client, userdata, flags, rc):                # function for making connection
    global connflag
    print ("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Function for Sending msg
    print(msg.topic+" "+str(msg.payload))
    
    

 
#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### These parameters are for Luis' aws endpoint ####
awshost = "atgk2cc4hnfq5-ats.iot.us-west-2.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.   
clientId = "rp"                                     # Thing_Name
thingName = "rp"                                    # Thing_Name
caPath = "/home/pi/certs/Amazon-root-CA-1.pem"                                      # Root_CA_Certificate_Name
certPath = "/home/pi/certs/device.pem.crt"                            # <Thing_Name>.cert.pem
keyPath = "/home/pi/certs/private.pem.key"                          # <Thing_Name>.private.key
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_start()                                          # Start the loop
 
while 1==1:
    #on connection 
    if connflag == True:
        #format results
        paylodmsg_json = json.dumps(ot_readings())
	#publish to topic
        mqttc.publish("topic", paylodmsg_json , qos=1)        # topic: temperature # Publishing Temperature values
        print("msg sent: Temps" ) # Print sent temperature msg on console
        print(paylodmsg_json)
    else:
        print("waiting for connection...")                      
    sleep(300)
