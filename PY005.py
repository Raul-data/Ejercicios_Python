# Dada una lista de palabras, filtra aquellas que comienzan con una letra dada por el usuario, sin método startswith(letra)

palabras = ["sol", "luna", "mar", "estrella", "cielo"] 
nuevas_palabras = []
letra_usuario = input("Dime una letra para darte las palabras que salen en la lista con esa letra: ")

for palabra in palabras:
    if palabra[0] == letra_usuario:
        nuevas_palabras.append(palabra)

# Verificar después del bucle si se encontraron palabras
if nuevas_palabras:  # Si la lista no está vacía
    print(nuevas_palabras)
else:
    print("La letra no coincide con ninguna palabra")
