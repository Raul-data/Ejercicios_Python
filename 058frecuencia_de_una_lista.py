# Crea una lista de números y cuenta cuántas veces aparece cada número en la lista, sin utilizar métodos de python.
# lista = [ 1, 2, 3, 3]
# 1:1
# 2:1
# 3:2

numeros = [1, 2, 3, 2, 4, 2, 5, 3, 2, 1, 2]
vacia = []
for i in numeros:
    if i not in vacia:
        vacia += [i]
        contador = 0
        for j in numeros:
            if j == i:
                contador += 1
        print(f"{i} : {contador}")