# Crea un diccionario con 5 productos y su precio. Pide un porcentaje de descuento al usuario y genera un nuevo diccionario con los precios rebajados.

# for producto, precio in productos.items():
#     precio_final = precio * (1 - descuento) 
#     productos_descuento[producto] = round(precio_final, 2)

productos = {
    "pan": 1.50,
    "leche": 0.95,
    "huevos": 2.30,
    "arroz": 1.20,
    "manzanas": 2.50
}

descuento = float(input("Introduce el descuento en %: ")) / 100

productos_descuento = {}

for producto, precio in productos.items():
    precio_final = precio * (1 - descuento)
    productos_descuento[producto] = round(precio_final, 2)
    
print(productos_descuento)