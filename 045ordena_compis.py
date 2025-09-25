# Guarda en una lista los nombres de 5 compañeros y ordénala alfabéticamente.

lista = ["raul","juan","sebi","guille"]

for i in range(len(lista)):
    for j in range(len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            aux = lista[j + 1]
            lista[j + 1] = lista[j]
            lista[j] = aux

print(lista)