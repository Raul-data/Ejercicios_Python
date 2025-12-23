# Tienes un catálogo en un diccionario:

# catalogo = {"pan":1.2, "leche":1.5, "huevos":2.3, "arroz":1.1}

# El usuario puede crear varias cestas de compra (identificadas como “cesta1”, “cesta2”…).
# Cada cesta será un diccionario con productos y cantidades.

# Al final, muestra el precio total de cada cesta y cuál es la más cara.

catalogo = {"pan": 1.2, "leche": 1.5, "huevos": 2.3, "arroz": 1.1}

cestas = {}

nombre_cesta = ""

while nombre_cesta != "fin":
    nombre_cesta = input("Nombre de la cesta o fin para finalizar la compra: ")
    
    if nombre_cesta != "fin":
        cesta = {}
        producto = ""
        
        while producto != "fin":
            producto = input("producto o fin: ")
            
            if producto != "fin":
                cantidad = int(input("Cantidad: "))
                cesta[producto] = cantidad
                
        cestas[nombre_cesta] = cesta
        
cesta_mas_cara = ""
precio_max = 0

for nombre in cestas:
    total = 0
    for producto in cestas[nombre]:
        total += catalogo[producto] * cestas[nombre][producto]
        
    print(f"{nombre} total: {total}")
    
    if total > precio_max:
        precio_max = total
        cesta_mas_cara = nombre
        
print(f"la cesta mas cara es: {cesta_mas_cara}")