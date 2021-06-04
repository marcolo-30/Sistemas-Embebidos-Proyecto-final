#!/bin/bash

sleep 60 

while true

do
    sensor=$(cat /dev/ttyAMA0 | grep GPGGA) 
    if [ -z "$sensor" ]
      
    sleep 120 
    
    if [ -z "$sensor" ]
    
    then
        sudo reboot 
    fi
    
    else
        sleep 120 
    fi
    
done
