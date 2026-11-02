import os
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def enviar_alerta(mensaje):
    webhook = os.environ.get("BRAINROT_WEBHOOK")
    
    if not webhook:
        print("No se encontró el webhook.")
        return False
      
     datos = json.dumps({
         "content": mensaje
     }).encode("utf-8")

     solicitud = Request(
         webhook,
         data=datos,
         headers={
             "Content-Type": "application/json",
             "User-Agent": "Mozilla/5.0"
         },
         method="POST"
     )    

     try:
         with urlopen(solicitud, timeout=10):
             print("Alerta enviada a Discord.")
             return True
             
     except (HTTPError, URLError) as error:
         print("No se pudo enviar la alerta:", error)
         return False
