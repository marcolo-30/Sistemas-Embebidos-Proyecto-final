#################################################################
###  Utilizando los scripts de lectura de GPS y acelerometro  ###
###  captura la informacion y la guarda en un archivo .csv    ###
#################################################################

import acc as Acc
import gps as GPS
import subprocess
from datetime import datetime

def captura_datos():
	try:
	        now = datetime.now()
	        hora_dato = now.strftime("%Y%m%d:%H:%M:%S")
	        posicion = GPS.obtener_posicion()
	        #print(posicion)
	        valores=Acc.obtener_datos()
	        #print(valores)
		dato=hora_dato+';'+posicion+';'+valores
       		print(dato)
		f = open("/home/pi/Final/datos.csv",'a')
		f.write(dato+'\n')
		f.close
	except:
		print("error")
def nuevo_archivo():

	subprocess.call(['bash','./guardar.sh'])


def	capture():
    print("Capturando datos con el siguiente formato: Fecha;Latitud;Longitud;Accx;Accy;Accz")
    while True:
        
        
            for i in range(61):
                captura_datos()
            nuevo_archivo()

