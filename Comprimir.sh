#! /bin/bash

file=./Carpeta_temp/
key=./llaves
name=$(date +"%Y-%m-%d-%H:%M")_data.enc

if [ ! "$(ls ~/Final/Carpeta_temp/)" ]
then
	encontrado=0

else



tar -czvf carpeta.tar.gz $file
echo archivo comprimido.

openssl enc -aes-256-cbc -salt -pbkdf2 -in carpeta.tar.gz -out $name -pass file:$key/aesKey.txt

echo archivo encriptado.
rm carpeta.tar.gz


echo "encriptando llave por defecto con llave Publica recibida"
openssl rsautl -encrypt -inkey $key/public.pem -pubin -in $key/aesKey.txt -out aesKey.txt.crypted

echo llave encriptada
mv ./Carpeta_temp/*.csv ./Backuparchivos
mv $name ./Carpeta_envio
mv aesKey.txt.crypted ./Carpeta_envio
fi
