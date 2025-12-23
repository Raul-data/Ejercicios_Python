# Genera un diccionario donde claves sean nombres de puntos (“A”, “B”, “C”… ) y valores una tupla con sus coordenadas (x, y). Muestra el punto más alejado del origen.

puntos = {
    "A": (2, 6),
    "B": (4, 7),
    "C": (2, 3)
}

punto_mas_lejano = ""
distancia_max = -1

for punto in puntos:
    x = puntos[punto][0]
    y = puntos[punto][1]
    distancia = x**2 + y**2
    
    if distancia > distancia_max:
        distancia_max = distancia
        punto_mas_lejano = punto

print(f"Punto mas lejano: {punto_mas_lejano}")