import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({
       "nombre": "Brainrot Hub",
       "estado": "Conectado",
       "version": "1.0"
  
  })
  
@app.route("/status")
  def status():
      return jsonify({
          "servidor": "Activo",
          "discord": "Configurado"
    
    })
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
