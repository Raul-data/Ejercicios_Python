# Dada una lista de palabras, filtra aquellas que comienzan con una letra dada por el usuario, sin método startswith(letra)

palabras = ["sol", "luna", "mar", "estrella", "cielo"] 
nuevas_palabras = []
letra_usuario = input("Dime una letra para darte las palabras que salen en la lista con esa letra: ")
for i in palabras:
    for j in i:
        if j == letra_usuario[0]:
            nuevas_palabras.append(i)
print(nuevas_palabras)
tys
,delattr



VOlver a mirar