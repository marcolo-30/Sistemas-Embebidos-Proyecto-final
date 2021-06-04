#! /bin/bash




if [ ! "$(ls ~/Final/Carpeta_envio/)" ]
then
	enviado=0
else 




scp ~/Final/Carpeta_envio/* marcolo@192.168.1.109:~/Escritorio/Server

if [ $? -eq 0 ];
then
	echo "Archivos enviados"
	mv ~/Final/Carpeta_envio/* ~/Final/Archivos_enviados

else
    echo "No se pudo enviar archivo"
fi

#scp aesKey.txt.crypted  marcolo@192.168.0.15:~/Escritorio/Server

fi
