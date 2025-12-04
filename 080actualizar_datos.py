#Dado un diccionario con información de un producto (nombre, precio, stock), pide al usuario un nuevo precio y actualízalo.
producto = {
    "nombre": "play5",
    "precio": 200,
    "stock": 23
}

print(f"Este es el producto: {producto}")

nuevo_precio = int(input("dime un nuevo precio del producto: "))

producto["precio"] = nuevo_precio

print(f"El producto con el nuevo precio: {producto}")