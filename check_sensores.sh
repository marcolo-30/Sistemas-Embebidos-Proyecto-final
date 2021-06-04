#!/bin/bash

sleep 60        #Espera mientras inicia y se configura el sistema.

while true

do
    sensor=$(cat /dev/ttyAMA0 | grep GPGGA)  #verifica si el GPS tiene conexion
    
    if [ -z "$sensor" ]          #Verifica por primera vez
      
    sleep 60 
    
    if [ -z "$sensor" ]          #verifica por segunda vez despues de dos minutos si no se encuentra el GPS reinicia la Rpi
    
    then
        sudo reboot 
    fi
    
    else
        sleep 120                #vuelve a realizar la verificacion cada 2 minutos. 
    fi
    
done
