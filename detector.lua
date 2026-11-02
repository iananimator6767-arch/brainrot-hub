local Detector = {}

Detector.Events = {}

function Detector.RegisterEvent(player, eventName, details)
    local event = {
        playerName = player.Name,
        userId = player.UserId,
        eventName = eventName,
        details = details or "Sin detalles",
        timestamp = os.time()
    }    
  
    table.insert(Detector.Events, event)
  
    print("[BRAINROT HUB] Evento detectado:")
    print("Jugador: " .. event.playerName)
    print("Evento: " .. event.eventName)
    print("Detalles: " .. event.details)
  
    return event
end
  
return Detector
