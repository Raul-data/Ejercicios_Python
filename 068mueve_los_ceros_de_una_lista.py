# Desplaza todos los ceros de una lista al final, sin alterar el orden de los otros números. Usad esta lista 

# numeros = [0, 1, 0, 3, 12, 0, 5] --> resultado final --> [1, 3, 12, 5, 0, 0 ,0]

numeros = [0, 1, 0, 3, 12, 0, 5]

for i in numeros:
    if i == 0:
        numeros.remove(i)
        numeros.append(i)
print(numeros)