### Script principal ###

import recoge_datos 
import subprocess
import requests
import os
import time
from multiprocessing import Process, Queue
import acc as Acc
import gps as GPS
from datetime import datetime

def captura_datos():   # Función para capturar los datos de los sensores y guardarlos en un archivo csv
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
		
def nuevo_archivo():  # Función para guardar el archivo en la carpeta temporal. 

	subprocess.call(['bash','./guardar.sh'])


def	capture(stop): #funcion que define si se siguen capturando datos o para por espacio lleno en el file system.
    print("Capturando datos con el siguiente formato: Fecha;Latitud;Longitud;Accx;Accy;Accz")
    while True:
        a=stop.get()
        if a==0:
            for i in range(61):
                captura_datos()
            nuevo_archivo()
        else:
            print("se lleno el file system")
            


def get_size(start_path):  #Función para obtener el tamaño de la carpeta donde se almacenan los archivos encriptados para enviar.
    
    try:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size
    except:
        print("Ya hay espacio reestableciendo toma de datos")

def check_carpeta(stop):  #Funcion para evaluar si la carpeta pasa el limite de peso establecido por el usuario para nuestro ejemplo 4 archivos. 
    while True:
        tam=get_size('./Carpeta_envio')
        
        if tam >= 3000:
            stop.put(60)
            time.sleep
        else:
            stop.put(0)
            time.sleep(60)
        
def check_sensores(): # Función que revisa el estado de conexión del GPS en caso de que no lo detecte por mas de dos minutos reinicia el sistema.
	
	while True:
    
        	subprocess.call(['bash','./check_sensores.sh'])

	
def internet_conect(q): # Función para evaluar si hay acceso a internet. 
    while True:
        try:
            request = requests.get("https://www.google.com", timeout=5)
        except (requests.ConnectionError, requests.Timeout):
            	q.put(0)
		#time.sleep(500)
	 	
        else:
            q.put(1)

def envia(q): #Funcion para enviar los datos mediante scp al servidor.

	while True:
		conexion=q.get()
		if conexion==1:
            		subprocess.call(['bash','./enviar.sh'])

def comprime(): #Función que comprime y encripta el archivo a enviar con su correspondiente llave. 

    while True:
    
        subprocess.call(['bash','./Comprimir.sh'])


if __name__ == "__main__":
    
    q  = Queue() #Cola para intercambiar información entre procesos referente a la conexión de internet. 
    stop= Queue() #Cola para intercambiar información referente al estado de ocupación del file system. 
    
    p1 = Process(target=internet_conect, args=(q,))
    p2 = Process(target=check_carpeta, args=(stop,))
    p3 = Process(target=capture, args=(stop,))
    p4 = Process(target=comprime, args=())
    p5 = Process(target=envia, args=(q,))
    p6 = Process(target=check_sensores, args=())
	
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()


    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
