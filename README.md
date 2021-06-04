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


## Pruebas


| Lenguaje      | Programa |
| ------------- | ------------- |
| C/C++, libreria Wiring Pi  | [Wiringpi](https://github.com/Fredycuellar/Proyecto1_Sistemas_Embebidos/blob/94931f9a6c48a0345d5b23ea3d00ba4b70d7f1ef/WiringPi) |
| C/C++, libreria BCM |[BCM](https://github.com/Fredycuellar/Proyecto1_Sistemas_Embebidos/blob/17cf8d916295f7ada7c51e401e840512e4fff93e/BCM_) |
| Python | [Python](https://github.com/Fredycuellar/Proyecto1_Sistemas_Embebidos/blob/5f52e727b520e943d16d735efebd35be09166315/Python)  |
|bash | [Bash](https://github.com/Fredycuellar/Proyecto1_Sistemas_Embebidos/blob/d43c243f8bea0d57bbbf3a5e0e3c35a0b7ee1acd/Bash) |



La conexión para el primer objetivo, para realizar la prueba se realiza el montaje con un led, teniendo en cuenta que la tarjeta raspberry Pi 2 Model B V1.1:

![Montajeled](https://user-images.githubusercontent.com/80786325/111538703-01537900-873b-11eb-9fce-9075bfeef7d4.PNG)

La conexión del sensor ds18b20,en la tarjeta raspberry Pi 2 Model B V1.1, es el siguiente:

![ConexionSensor (1)](https://user-images.githubusercontent.com/80786325/111538879-39f35280-873b-11eb-8fee-31c0a53a4f96.PNG)

A continuación, se indica la programación implementada para el primer objetivo:

| Lenguaje      | Programa |
| ------------- | ------------- |
| C/C++, libreria Wiring Pi  | [Wiringpi](https://github.com/Fredycuellar/Proyecto1_Sistemas_Embebidos/blob/94931f9a6c48a0345d5b23ea3d00ba4b70d7f1ef/WiringPi) |
| C/C++, libreria BCM |[BCM](https://github.com/Fredycuellar/Proyecto1_Sistemas_Embebidos/blob/17cf8d916295f7ada7c51e401e840512e4fff93e/BCM_) |
| Python | [Python](https://github.com/Fredycuellar/Proyecto1_Sistemas_Embebidos/blob/5f52e727b520e943d16d735efebd35be09166315/Python)  |
|bash | [Bash](https://github.com/Fredycuellar/Proyecto1_Sistemas_Embebidos/blob/d43c243f8bea0d57bbbf3a5e0e3c35a0b7ee1acd/Bash) |
