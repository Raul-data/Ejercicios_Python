# Encuentra el valor máximo de una lista de números sin usar la función max()
numeros = [2,3,5,6,3,45,62,22]
maximocon = numeros[1]

for i in numeros:
    
    if maximocon <= i:
        
        maximocon = i
print(maximocon)