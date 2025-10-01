# Calcula la media de los números de una lista. La media es la suma de todos los elementos partido por el número total de elementos.

numeros = [2,3,5,6,3,45,62,22]
aux = 0
for i in range(len(numeros)):
    aux += numeros[i]
    
aux = aux / len(numeros)
    
print(f"La media de los nuemeros {numeros} es: {aux}")