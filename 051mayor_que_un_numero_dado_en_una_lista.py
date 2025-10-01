# Dada una lista con 20 números, el programa localizará los valores mayores, no iguales, que un número dado por el usuario. Finalmente mostrará ordenados de menor a mayor los valores que cumplan la condición y el valor mayor de todos.
numeros = [3, 7, 12, 18, 25, 31, 37, 44, 50, 57, 63, 70, 77, 83, 90,96,15,41,68,99]
num_usuario = int(input("Dime un numero para ver si esta el numero en la lista: "))
numero_nuevo = []


for i in range(len(numeros)): 
    if num_usuario < numeros[i]:
        numero_nuevo.append(numeros[i])
        numero_nuevo.sort()

print(f"Estos son los numeros mas altos desde el numero que nos has dado: {numero_nuevo} ")