alto = 4
ancho = 6

for i in range(alto):
    if i == 0 or i == alto - 1:
        print("*" * ancho)
    else:
        print("*" + (" " * (ancho - 2)) + "*")
