# Sistemas-Embebidos-Proyecto-final

<p align="Center">
  <img width="400" height="280" src="https://user-images.githubusercontent.com/84221113/120844998-d0166800-c535-11eb-8224-03487d0d735f.png">
</p>

El proyecto final consiste en proponer una solucion a un problema de ingeniería que involucre el uso de un sistema embebido como sistema central de procesamiento.

Para esto se desarrolla una solución IoT para rastrear la posicion de un vehiculo y sus valores de aceleracion durante los recorridos que realice, guardando los datos de los sensores en un archivo .csv, encriptandolos, y enviandolos a un servidor de almacenamiento de información. 

<p align="center">
  <img width="400" height="400" src="https://user-images.githubusercontent.com/84221113/120840693-2bddf280-c530-11eb-9e73-0eb4891f7ace.png">
</p>


Para el desarrollo del proyecto se requiere:

- Crear y ejecutar scripts diferentes encargados de tareas específicas, de esta forma se aplicaran multiproceso en el sistemas embebidos.

- Comunicar los scripts por archivos en disco siempre y cuando la actualización de estos "escritura sobre el mismo archivo" no sea muy alta, por ejemplo uno cada minuto 

- Supervisar el tamaño de las carpetas que se usa para guardar los archivos temporales, si esta sube de un cierto tamaño deben tomar medidas para evitar el colapso del file system. 

El protocolo de pruebas es el siguiente:

- Simular una caída de internet y el sistema se debe reponer solo cuando vuelva la conexión. Mientras esto pasa el sistema debe ir llenando la cola hasta que que tamaño máximo de la carpeta previamente configurado lo permita, si se llena esta carpet(a/as) la captura de datos debe detenerse pero el proceso de envío debe seguir reintentando desocuparlas. 

- Desconectar la fuente de datos (sensor, cámara, archivo, etc...) el sistema debe reintentar hasta que se conecte de nuevo y debe continuar el funcionamiento.

- Desconectar la potencia de la tarjeta es decir quitarle fuente. simulando una falla eléctrica, después vuelvo a conectar y todo debe funcionar normalmente.

## Diagrama

Para el desarrollo del proyecto se utiliza:
- RaspberryPi3
- GPS Neo 6m
- Accelerometro ADXL345
- Servidor(Pc Personal)

<p align="center">
  <img width="600" height="400" src="https://user-images.githubusercontent.com/84221113/120865759-42964080-c554-11eb-902d-889f7eca7427.png">
</p>

## Desarrollo

Se crean 6 procesos en la ejecucion del programa principal:

| Proceso      | Script |
| ------------- | ------------- |
| Revisar la conexion de internet | [internet.py](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto-final/blob/main/internet.py) |
| Revisar la ocupación de la carpeta temporal (Fyle System) |[peso_carpeta.py](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto-final/blob/main/peso_carpeta.py) |
| Capturar los datos de los sensores y guardarlos en un archivo .csv | [recoge_datos.py](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto-final/blob/main/recoge_datos.py)  |
|Comprimir los archivos. | [Comprimir.sh](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto-final/blob/main/Comprimir.sh) |
| Enviar los archivos comprimidos al servidor | [enviar.sh](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto-final/blob/main/enviar.sh)  |
|Revisar la conexión de los sensores.| [check_sensores.sh](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto-final/blob/main/check_sensores.sh) |
| Script principal | [main.py](https://github.com/marcolo-30/Sistemas-Embebidos-Proyecto-final/blob/main/main.py)  |


## Pruebas

Se muestran los videos de las pruebas del funcionamiento del proyecto 

| Prueba      | Video |
| ------------- | ------------- |
| Funcionamiento general  | [General](https://www.youtube.com/watch?v=8SYreTL2sc0) |
| Desconexión de sensores y fuente de alimentación|[Desconexiones](https://www.youtube.com/watch?v=aT4Dv9etTH8) |
| Desconexión Internet | [Desconexión internet](https://www.youtube.com/watch?v=g9UHI5J2HCA)  |
| Llenado del File System | [Llenado File system](https://www.youtube.com/watch?v=vMP-sZkJT6s) |

### Nota:
Los videos de desconexión Internet y llenado de fyle system no poseen audio ya que se grabo directamente el escritorio de la raspberry pi sin tener conexión de audio, en los videos se muestra el funcionamiento del dispositivo cuando no cuenta con conexión a internet. 

- En el video de desconexion de internet se desconecta la opcion del wifi en los primeros segundos, se crean y encriptan los archivos al segundo 00:38, se reconecta el wifi al segundo 00:56 y se envian los documentos al servidor al segundo 1:08  se recomienda ver el video con velocidad de reproducción X2. 
- En el video correspondiente al llenado del file system, se inicia el video con el wifi desconectado y tres archivos encriptados a la espera de ser enviados cuando se reconecte el internet, en el segundo 00:20 se genera un nuevo archivo encriptado el cual supera el limite de capacidad fijado y se observa sobre el script el mensaje de "file system lleno" interrumpiendo la captura de los datos hasta que se libere espacio, esto después de establecer conexión nuevamente con internet y enviar los archivos liberando espacio en la carpeta. 

## Conclusiones 
- El uso de multiprocesamiento facilita la ejecución de scripts en paralelo.
- Teniendo en cuenta de que los procesos no utilizan el mismo espacio de memoria el uso de colas permite realizar transferencia de informacion entre procesos. 
- Para la protección de los datos se puede cifrar la micro SD utilizando LUKS y Kali como se puede evidenciar en el siguiente link https://www.redeszone.net/raspberry-pi/proteger-raspberry-pi-cifrando-datos-luks-kali-linux/

