# Dibujar la letra S con S
for fila in range(7):          # 7 filas
    for columna in range(5):   # 5 columnas
        # Condiciones para la forma de la S
        if ((fila == 0 and columna > 0)                      # parte de arriba
            or (fila == 3 and columna > 0 and columna < 4)   # parte del medio
            or (fila == 6 and columna < 4)                   # parte de abajo
            or (columna == 0 and fila > 0 and fila < 3)      # lado izquierdo arriba
            or (columna == 4 and fila > 3 and fila < 6)):    # lado derecho abajo
            print("S", end="")
        else:
            print(" ", end="")
    print()
