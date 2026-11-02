local Logic = {}

function Logic.formatItemNotice(playerName, itemName)
    return string.format(
        "Jugador: %s | Objeto: %s",
        tostring(playerName),
        tostring(itemName)
    )
end

return Logic
