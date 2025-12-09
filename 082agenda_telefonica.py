# Crea un diccionario con 5 nombres y sus teléfonos. Permite buscar un nombre y mostrar su número. Si no existe, mostrar mensaje adecuado.

datos = {
    "euralia" : 56663453,
    "eufasio" : 53234262,
    "frisea" : 2342623,
    "eugilio" : 223422,
    "perfasio" : 2341123
}

nombre = input("Introduce un nombre: ")

if nombre in datos:
    print(f"El telefono de {nombre} es {datos[nombre]}")
else:
    print("ese nombre no esta en la agenda")