### Script para evaluar el peso de la carpeta ###
# retorna el valor en bytes del peso de la carpeta

import os
def get_size(start_path = './Carpeta_envio'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

print get_size()
