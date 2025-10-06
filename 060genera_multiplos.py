# Pide al usuario un número y genera una lista con sus primeros n múltiplos, donde n también es dada por el usuario.

num_usuario = int(input("Dime un numero para generar la lista de multiplos: "))
n = int(input("Dime de cuantos multiplos lo quieres: "))
multiplos = []

for i in range(n):
    multiplos += [num_usuario * (i +1)]

print(f"Los primeros {n} multiplos de {num_usuario} son: {multiplos}")