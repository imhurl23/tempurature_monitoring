# Continuous Remote Fermentation Monitoring System 

This system is a remote tempurature monitoring setup. By running scripts on a raspberry pi this project creates a remote access point in the form of a web application to view updating tesmpurature data. 
## Description

This code base paired with a configured raspberry pi product and tempurature sensors can be used to help ensure safe at home fermentation. 

## Getting Started
For information on how to run the scripts on the raspberrry pi: https://docs.google.com/document/d/1xA-vdfHDePmcq0FVDPCigT55Rxa6r-Ud1ls8NACyue4/edit?usp=sharing
Once, this is complete you can simply view the webpage: http://54.196.10.228:8000/ (Note: this may not be live at all points in time. If you are interested in running an experiment please coordinate with Luis and Izzy to get a hold of the sensors and make sure the web app is running)


### Dependencies

* The configurations and instructions are based on running the "client" with a MacOS. The prototype raspberry pi must have Full Raspberry Pi OS. 

### Installing
#### To connect to and run code on the pi (as reference in the instruction document: https://docs.google.com/document/d/1xA-vdfHDePmcq0FVDPCigT55Rxa6r-Ud1ls8NACyue4/edit?usp=sharing )
* download temps.sh and follow the instructions outline in the document 

#### To replicate our work: 
* The RaspberryPiCode is to be downloaded onto the home folder of a raspberry pi device with configured tempurature sensors. See (https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/#:~:text=Connect%20pin%201%20to%20the,your%20finger%20against%20the%20sensor.) for tempurature sensor setup. Place all these code files in the home folder of the pi. 
* If you would like to create a similar webpage: the django_webpage directory contains all necessary code and can be deployed on different severs. We used an AWS lightsial server.




## Authors

Contributors names and contact info

Izzy Hurley 
[@IzzyHurley](imhurl23@colby.edu)
Luis Baez
[@LuisBaez](lmbaez23@colby.edu)



## Acknowledgments

Inspiration from: 
* [AWS IOT SKDS](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html)
* [Circuit Basics: Raspberry Pi Troubleshooting Tutorial](https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/)
* [WSN for wine fermentation](https://digitalcommons.calpoly.edu/cpesp/58/)
