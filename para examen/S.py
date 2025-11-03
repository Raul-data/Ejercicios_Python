ancho = int(input("Ancho de la S: "))
alto = int(input("Alto de la S (debe ser impar): "))

# Aseguramos que alto sea impar y mínimo 5
if alto % 2 == 0:
    alto += 1
if alto < 5:
    alto = 5

mitad = alto // 2

for i in range(alto):
    if i in [0, mitad, alto - 1]:           # Líneas horizontales
        print("*" * ancho)
    elif i < mitad:                          # Parte superior: borde izquierdo
        print("*" + " " * (ancho - 1))
    else:                                    # Parte inferior: borde derecho
        print(" " * (ancho - 1) + "*")