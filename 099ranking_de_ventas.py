# Tienes una lista de ventas del tipo:

# [("Pepe", 200), ("Juanito", 150), ("Pitingo", 50), ("Optimus_Prime", 300), ("Pitingo", 50), ("Optimus_Prime", 300), ("Juanito", 150)...]

# Construye un diccionario donde clave = vendedor y valor = suma total de ventas.

# Muestra el ranking ordenado de mayor a menor usando sorted() con key=.

ventas = [
    ("Pepe", 200),
    ("Juanito", 150),
    ("Pitingo", 50),
    ("Optimus_Prime", 300),
    ("Pitingo", 50),
    ("Optimus_Prime", 300),
    ("Juanito", 150),
]

diccionario_ventas = {}

for i in range(len(ventas)):
    vendedor = ventas[i][0]
    cantidad = ventas[i][1]

    if vendedor not in diccionario_ventas:
        diccionario_ventas[vendedor] = cantidad
    else:
        diccionario_ventas[vendedor] += cantidad

print("Ventas totales:", diccionario_ventas)

# Ranking de mayor a menor
ranking = dict(sorted(diccionario_ventas.items(), key=lambda x: x[1], reverse=True))

print("Ranking:", ranking)