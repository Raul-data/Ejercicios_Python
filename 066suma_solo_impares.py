# Suma únicamente los números impares de una lista de números enteros dada por el usuario.

numeros = [1,2,3,4,5,6,7,8,9]
impares = 0


for i in numeros:
    
    if i % 2 != 0:
        impares += i
        
print(impares)

