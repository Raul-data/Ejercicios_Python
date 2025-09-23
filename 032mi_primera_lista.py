# Crea una lista con números enteros dados por el usuario. Luego, imprime el primer y último elemento.
mi_lista = []

while True:
    dato = input("Introduce un dato (o escribe 'fin' para terminar): ")
    if dato.lower() == 'fin':
        break
    mi_lista.append(dato)
    
print(f"los datos que has dado son: {mi_lista}")