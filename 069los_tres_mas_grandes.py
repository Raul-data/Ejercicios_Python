# Encuentra los tres números más grandes de una numeros sin modificar la numeros original. Usad esta numeros numeros = [10, 30, 15, 2, 45, 60, 5, 100, 35].

numeros = [10, 30, 15, 2, 45, 60, 5, 100, 35]
lista_final = []

numeros.sort()

for i in numeros:
    lista_final = numeros[-3:]
print(lista_final)
