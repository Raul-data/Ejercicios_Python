tam = 7
for i in range(tam):
    fila = ""
    for j in range(tam):
        # Columna izquierda: siempre *
        if j == 0:
            fila += "*"
        # Líneas horizontales: toda la fila *
        elif i == 0 or i == tam // 2:
            fila += "*"
        # Diagonal inferior: solo en la posición correcta
        elif i > tam // 2 and j == i - 2:
            fila += "*"
        # Columna derecha: SOLO en filas 0, 1, 2, 3 (no en diagonal)
        elif j == tam - 1 and i <= tam // 2:
            fila += "*"
        # Espacios en el resto
        else:
            fila += " "
    print(fila)