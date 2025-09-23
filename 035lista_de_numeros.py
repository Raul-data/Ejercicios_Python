# Crea una lista vacía llamada numeros y agrega los números del 1 al 1000 usando el método append(). Luego imprime la lista.

numeros = []
contador = 1

while contador <= 100:
    numeros.append(contador)
    contador += 1

print(numeros)