# Crea una lista con los números [5, 2, 9, 1, 5, 6]. Ordena la lista en orden ascendente y descendente.

numeros = [5, 2, 9, 1, 5, 6]

for i in range(len(numeros)):
    for j in range(len(numeros)-i-1):
        if numeros[j]>numeros[j+1]:
            aux = numeros[j+1]
            numeros[j+1] = numeros[j]
            numeros[j] = aux

print(numeros)
print(numeros[::-1])