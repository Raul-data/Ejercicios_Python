# Crea una lista de números. Divide la lista en dos nuevas listas: una que contenga los números menores que un número dado por el usuario y otra que contenga los números mayores o iguales al número dado.

num_dado = int(input("Dime un numero para darte los mas pequeños y los mayores de la lista: "))
lista_numeros = [1,2,3,4,5,6,7,8,9]
lista_menor = []
lista_mayor = []

for i in range(len(lista_numeros)):
    if i < num_dado:
        lista_menor.append(i)
    else:
        lista_mayor.append(i)
        
print(f"tu numero es {num_dado} esta es la lista menor: {lista_menor} y esta es la mayor: {lista_mayor}")