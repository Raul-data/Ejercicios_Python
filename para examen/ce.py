ancho = 4
alto = 5

for i in range(alto):
    if i == 0:
        print("*" * ancho)
    elif i == alto - 1:
        print("*" * ancho)
    else:
        print("*" + (" " * (ancho - 2)))