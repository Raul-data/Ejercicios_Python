# Dibujar la letra R con R
for fila in range(7):          # 7 filas
    for columna in range(5):   # 5 columnas
        # Condiciones para formar la forma de la R
        if (columna == 0                                     # línea izquierda
            or (fila == 0 and columna < 4)                   # línea superior
            or (fila == 3 and columna < 4)                   # línea del medio
            or (columna == 4 and fila > 0 and fila < 3)      # línea derecha arriba
            or (fila - columna == 3 and fila > 2)):          # diagonal de la pierna
            print("R", end="")  # imprime sin salto de línea
        else:
            print(" ", end="")  # espacio vacío
    print()  # salto de línea al final de cada fila
