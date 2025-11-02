alto = int(input("Dime el alto: "))
ancho = int(input("Dime el ancho: "))

for i in range(alto):
    if i == 0 or i == alto - 1:
        print("*" * ancho)
    else:
        print("*" + (" " * (ancho - 2)) + "*")
