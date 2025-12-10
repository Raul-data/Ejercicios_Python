# Pide al usuario que introduzca productos y precios hasta que escriba “fin”. Guarda todo en un diccionario e imprime el total de productos y la suma de precios.

producto = ""
productos = {}

while producto != "fin":
    producto = input("Introduce un producto (o fin para finalizar): ")
    
    if producto != "fin":
        precio = int(input("introduce precio:"))
        productos[producto] = precio
        
print(productos)        
