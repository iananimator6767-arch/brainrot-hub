from flask import Flask, request, jsonify
from discord_alerts import enviar_alerta

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
    
@app.route("/alert", methods=["POST"])
def alert():
    datos = request.get_json(silent=True) or {}
    
    jugador = datos.get("jugador")
    evento = datos.get("evento")
    
    if not isinstance(jugador, str) or not isinstance(evento, str):
        return jsonify({"error": "Datos incorrectos"}), 400
        
    mensaje = (
        "🚨 BRAINROT HUB\n"
        f"👤 Jugador: {jugador[:50]}\n"
        f"📋 Evento: {evento[:200]}"
    )
    
    if enviar_alerta(mensaje):
        return jsonify({"estado": "Alerta enviada"})
        
    return jsonify({"error": "No se pudo enviar"}), 502
    
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
