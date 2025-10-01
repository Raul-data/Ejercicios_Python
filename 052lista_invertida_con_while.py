# Crea una lista de números y utiliza un bucle while para invertir el orden de los elementos.

numeros = [2,3,5,6,3,45,62,22]
numeros_invertidos = []
pepe = len(numeros) - 1

while pepe >= 0:
     numeros_invertidos.append(numeros[pepe])
     pepe -= 1
     
print(f"La lista invertida : {numeros_invertidos}")