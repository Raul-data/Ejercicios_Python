ancho = int(input("cuanto quieres de ancho: "))
largo = int(input("Cuanto quieres de largo: "))

for i in range(ancho):
    if i == ancho - 1:
        print("*" * ancho)
    else:
        print("*" + (" " * (ancho - 2)) + "*")
for j in range(largo - 2):
    if i == 0:
        print("*" * largo -1)
    else:
        print("*" + (" " * (ancho - 2)) + "*")
    