### Rervisa si existe conexión a internet ###

import requests
try:
    request = requests.get("https://www.google.com", timeout=5)
except (requests.ConnectionError, requests.Timeout):
    print("Sin conexion a internet.")
else:
    print("Con conexion a internet.")
