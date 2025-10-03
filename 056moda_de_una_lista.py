# Calcular la moda de una lista. La moda es el valor más repetido en una lista.

lista = [1, 2, 3, 2, 4, 2, 5, 3, 2, 1, 2]
max_repeticiones = 0
moda = lista[0]

for i in lista:
    repeticiones = 0
    for j in lista:
        if j == i:
            repeticiones += 1
    if repeticiones > max_repeticiones:
        max_repeticiones = repeticiones
        moda = i

print(f"la lista seria {lista} y la moda es {moda}")