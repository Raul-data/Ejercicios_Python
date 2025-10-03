# La mediana de una lista es el número central de una lista ordenada. Si la lista tiene número par de elementos, se debe hacer la media aritmética de los elementos centrales para calcular su mediana. 

# Por ejemplo: 1 2 3 4 5 6 7 8 9 --> el cinco sería la mediana de esta lista. 1 2 3 4 5 6 7 8 9 10 --> 11/2=5.5 mediana buscada.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.sort()
n = len(numeros)

if n % 2 == 1:
    mediana = numeros[n // 2]
else:
    mediana = (numeros[n // 2 - 1] + numeros[n // 2]) / 2

print(f"La mediana de la lista de numeros {numeros} es: {mediana}")