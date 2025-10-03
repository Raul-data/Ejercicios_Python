# Pide al usuario que ingrese un número y reemplaza todas las apariciones de ese número en una lista por otro número dado por el usuario.

lista=[1,2,3,9,5,6,7,8,9]
numEliminar=int(input(f"dime el numero que desea cambiar de la lista {lista}: "))
numCambiar=int(input("Que numero desea poner: "))

for i in range(len(lista)):
    
    if lista[i]==numEliminar:
        lista[i]=numCambiar
        
print(lista)
