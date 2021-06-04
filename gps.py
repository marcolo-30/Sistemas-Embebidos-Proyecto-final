### Script para capturar los datos del GPS ###

import serial
import time
import string
import pynmea2
import sys
import subprocess
import time

def obtener_posicion():

	while True:
		try:
			port="/dev/ttyAMA0"
			ser=serial.Serial(port, baudrate=9600, timeout=0.5)
			dataout = pynmea2.NMEAStreamReader()
			newdata=ser.readline()

			if newdata[0:6] == "$GPRMC":
				newmsg=pynmea2.parse(newdata)
				lat=newmsg.latitude
				lng=newmsg.longitude
				gps = str(lat) + ";" + str(lng)
				return gps

		except:
			print(" No hay conexion con el gps ")
